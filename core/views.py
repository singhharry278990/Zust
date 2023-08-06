from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import  authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
from django.http import JsonResponse
# Create your views here.

@login_required
def index(request):
    user = User.objects.get(username=request.user.username)
    print(user)
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }
    print(user_obj)
    return render( request, 'index.html', {"user_obj":user_obj}  )

def birthday(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'birthday.html',  {"user_obj":user_obj})

def events(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'events.html',  {"user_obj":user_obj})

def favorite(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'favorite.html',  {"user_obj":user_obj})

def help_and_support(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'help-and-support.html',  {"user_obj":user_obj})

def forget_password(request):
    print(request.POST)
    return render( request, 'forgot-password.html' )

def friends(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'friends.html',  {"user_obj":user_obj})

def groups(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'groups.html',  {"user_obj":user_obj})

def live_Chats(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'live-chat.html',  {"user_obj":user_obj})

@csrf_exempt
def login(request):

    if request.POST:
        print(request.user)
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = User.objects.filter(username=username, is_superuser=False).first()
        if check_user:
            username = check_user.username
            user_obj = authenticate(username=username, password=password)
            if user_obj is not None:
                auth_login(request, user_obj)
                return HttpResponseRedirect('index')
            else:
                print("error")
    return render(request, 'login.html')


def marketplace(request):
    user = User.objects.get(username=request.user.username)
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'marketplace.html',  {"user_obj":user_obj})

@login_required
def messages(request):
    user = User.objects.get(username=request.user.username)
    pro_obj = Profile.objects.get(user=user)

    # Get the first username from the followers
    followers_username = pro_obj.followers.values_list('username', flat=True).first()

    # Get the first username from the following users
    following_username = pro_obj.following.values_list('username', flat=True).first()
    user_obj = {
        'username': user.username,
        'email': user.email,
        'fullname': user.first_name + ' ' + user.last_name,
        'following': following_username,
        'followers': followers_username
    }

    return render(request, 'messages.html', {"user_obj": user_obj})



def notifications(request):
    return render( request, 'notifications.html')


def myprofile(request):
    user = User.objects.get(username=request.user.username)
    if user:
        pro_obj = Profile.objects.get(user=user)

        user_obj = {
            'username': user.username,
            'email': user.email,
            'fullname': user.first_name + ' ' + user.last_name,
            'profile_pic_url': pro_obj.profile_pic.url,
            'cover_image_url': pro_obj.cover_image.url,
            "profile": pro_obj,
        }

    
    return render( request, 'my-profile.html', {"user_obj":user_obj})


def notifications(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }
    return render( request, 'notifications.html',  {"user_obj":user_obj})


def privacy(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }
    return render( request, 'privacy.html',  {"user_obj":user_obj})

def register(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(email, name, username, password)
        user_obj = User.objects.create(first_name=name, username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        return redirect('login')
    return render( request, 'register.html')

def tryile(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }
    return render( request, 'tryile.html',  {"user_obj":user_obj})


def video(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }
    return render( request, 'video.html',  {"user_obj":user_obj})


def weather(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }
    return render( request, 'weather.html',  {"user_obj":user_obj})
@login_required
def setting(request):
  
    user = User.objects.get(username=request.user)
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }
    
    return render( request, 'setting.html', {"user_obj":user_obj})



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def test(request):
    return render(request, "test.html")

def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})


def personal_info_view(request):
    if request.method == 'POST':

        # Access form data using request.POST dictionary
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        backup_email = request.POST.get('backup_email')
        date_of_birth = request.POST.get('datepicker')
        mobile_no = request.POST.get('mobile_no')
        website = request.POST.get('website')
        language = request.POST.get('language')[1]
        blood_group = request.POST.get('blood_group')
        relation_status = request.POST.get('relation_status')
        occupation = request.POST.get('occupation')
        country = request.POST.get('country')[1]
        state = request.POST.get('state')
        gender = request.POST.get('gender')
        user_obj = User.objects.filter(username=request.user)
        print(request.POST)
        if user_obj:
            user_obj.first_name = first_name
            user_obj.last_name = last_name
            user_obj.email = email
            user_obj.save()
            Profile.objects.filter(user=user_obj).create(backup_email=backup_email, birthday=date_of_birth, mobile_no=mobile_no,
                                                    website=website, state=state, language=language, blood_group=blood_group, relation_status=relation_status,
                                                    occupation=occupation, country=country, gender=gender,)

            # Return a JSON response indicating success
            return JsonResponse({'message': 'Data received successfully'})





def uploaded_image_view(request):
    if request.method == 'POST' and request.FILES.get('imageFile'):
        image_file = request.FILES['imageFile']
        user = User.objects.get(username=request.user.username)
        imageText = request.POST.get("imageText")
        print("Image:", request.POST)
        if user and image_file != '':
            pro_obj = Profile.objects.get_or_create(user=user)[0]
            if user and imageText:
                pro_obj.cover_image = image_file
            else:
                pro_obj.profile_pic = image_file

            pro_obj.save()

            return JsonResponse({'message': 'Image uploaded successfully'})
        else:
            return JsonResponse({'message': 'Upload the image again'})
    else:
        return JsonResponse({'message': 'Image upload failed'})

