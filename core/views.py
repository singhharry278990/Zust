from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login as auth_login

# Create your views here.
def index(request):
    return render( request, 'index.html')

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
        username = request.POST.get('username')
        password = request.POST.get('password')
        check_user = User.objects.filter(username=username).first()
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
    return render( request, 'my-profile.html')


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

def setting(request):
    return render( request, 'setting.html')

from django.http import HttpResponseRedirect

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')