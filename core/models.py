from django.db import models
from PIL import Image

from django.contrib.auth.models import User
# Create your models here.


class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField()

def upload_profile_to(instance,filename):
	return f'profile_picture/{instance.user.username}/{filename}'

def upload_cover_to(instance,filename):
	return f'coverImage/{instance.user.username}/{filename}'

class Profile(models.Model):
	gen = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	about_me = models.CharField(max_length=250, null=True)
	blood_groups = models.CharField(max_length=10, null=True)
	backup_email = models.EmailField()
	Occupation = models.CharField(max_length=250, null=True)
	Relation_status= models.CharField(max_length=50, null=True)
	Website = models.CharField(max_length=50,null=True, blank=True)
	language = models.CharField(max_length=30, null=True, blank=True)
	city = models.CharField(max_length=30, null=True, blank=True)
	state = models.CharField(max_length=30, null=True, blank=True)
	country = models.CharField(max_length=30, null=True, blank=True)
	mobile_no = models.CharField(max_length=30, null=True, blank=True)
	birthday = models.DateField(null=True)
	profile_pic = models.ImageField(upload_to = upload_profile_to, null=True, default = 'defaults/profile_pic.jpg')
	cover_image = models.ImageField(upload_to = upload_cover_to, null = True, default= 'defaults/cover_image.jpg')
	gender = models.CharField(choices=gen, max_length=6, null=True)
	followers = models.ManyToManyField(User, related_name='followers', blank=True)
	following = models.ManyToManyField(User, related_name="following", blank=True)

	def __str__(self):
		return self.user.username

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)

		img = Image.open(self.profile_pic.path)
		if img.height > 300 or img.width > 300:
			output_size = (300, 300)
			img.thumbnail(output_size)
			img.save(self.profile_pic.path)

		img2 = Image.open(self.cover_image.path)
		if img2.height > 500 or img2.width > 500:
			output_size = (500, 500)
			img2.thumbnail(output_size)
			img2.save(self.cover_image.path)

	def non_followed_user(self):
		return set(User.objects.filter(is_active=True))-set(self.following.all())-{self.user}

	def get_notifications(self):
		return Notification.objects.filter(user=self.user, seen = False)

class Notification(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	message = models.CharField(max_length=500)
	link = models.CharField(max_length=500)
	seen = models.BooleanField(default=False)

def upload_post_to(instance,filename):
	return f'post_picture/{instance.user.username}/{filename}'

class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	text = models.TextField()
	picture = models.ImageField(null=True, upload_to = upload_post_to,)
	created_at = models.DateTimeField(auto_now_add=True)
	likes = models.ManyToManyField(User,related_name='likes')
	dislikes = models.ManyToManyField(User,related_name='dislikes')



class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)

class Dislike(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)	

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()

class SubComment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	time = models.DateTimeField(auto_now_add=True)
	comm = models.TextField()
	comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


