from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [

    path('index/',views.index, name='index'),
    path('birthday/',views.birthday, name='birthday'),
    path('events/',views.events, name='events'),
    path('favorite/',views.favorite, name='favorite'),
    path('forget_password/',views.forget_password, name='forget_password'),
    path('friends/',views.friends, name='friends'),
    path('groups/',views.groups, name='groups'),
    path('help_support/',views.help_and_support, name='help_support'),
    path('register/',views.register, name='register'),
    path('',views.login, name='login'),
    path('live_chat/',views.live_Chats, name='live_chat'),
    path('marketplace/',views.marketplace, name='marketplace'),
    path('messages/',views.messages, name='messages'),
    path('profile/',views.myprofile, name='profile'),
    path('privacy/',views.privacy, name='privacy'),
    path('setting/',views.setting, name='setting'),
    path('tryile/',views.tryile, name='tryile'),
    path('video/',views.video, name='video'),
    # path('test/',views.test, name='test'),
    path("<str:room_name>/", views.room, name="room"),
    path('logout/',views.logout_view, name='logout'),
    path('weather/',views.weather, name='weather'),
    path('notifications/',views.notifications, name='notifications'),
    path('personal-info/',views.personal_info_view, name='personal-info'),



]
