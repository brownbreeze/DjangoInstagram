from django.urls import path, re_path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'), 
    path('logout/', views.logout, name='logout'), 
    path('signup/', views.signup, name='signup'),
    path('password_change/', views.password_change, name='password_change'),
    path('edit/', views.profile_edit, name='profile_edit'),
    re_path(r'^(?P<username>[\w.0+-]+)/follow/$', views.user_follow, name='user_follow'),
    re_path(r'^(?P<username>[\w.0+-]+)/unfollow/$', views.user_unfollow, name='user_unfollow'),
]
