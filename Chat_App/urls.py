from django.conf.urls import url
from django.urls import path, re_path
from . import views
app_name = 'chatapp'
urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.signupView, name='signupview'),
    path('login/', views.loginView, name='loginView'),
    path('adduser/', views.addUser, name='addUser'),
    url('chatmsg/', views.chatView, name='chatView'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
