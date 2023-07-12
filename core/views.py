from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import  authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from .models import *
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
    return render( request, 'birthday.html')

def events(request):
    return render( request, 'events.html')

def favorite(request):
    return render( request, 'favorite.html')

def help_and_support(request):
    return render( request, 'help-and-support.html')

def forget_password(request):
    print(request.POST)
    return render( request, 'forgot-password.html')

def friends(request):
    return render( request, 'friends.html')

def groups(request):
    return render( request, 'groups.html')

def live_Chats(request):
    return render( request, 'live-chat.html')

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
    return render( request, 'marketplace.html')


def messages(request):
    return render( request, 'messages.html')

def notifications(request):
    return render( request, 'notifications.html')


def myprofile(request):
    user = User.objects.get(username=request.user.username)
    
    user_obj = {'username': user.username,
                'email': user.email,
                'fullname':user.first_name + ' ' + user.last_name
                }

    return render( request, 'my-profile.html', {"user_obj":user_obj}  )


def notifications(request):
    return render( request, 'notifications.html')


def privacy(request):
    return render( request, 'privacy.html')

def register(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.create(first_name=name, username=username, email=email)
        user_obj.set_password(password)
        user_obj.save()
        return redirect('login')
    return render( request, 'register.html')

def tryile(request):
    return render( request, 'tryile.html')


def video(request):
    return render( request, 'video.html')


def weather(request):
    return render( request, 'weather.html')
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

from django.http import JsonResponse

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
