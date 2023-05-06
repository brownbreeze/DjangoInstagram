from django.urls import path, re_path
from django.contrib.auth.validators import UnicodeUsernameValidator
from . import views

app_name = 'instagram'

#username_regex = UnicodeUsernameValidator.regex
urlpatterns = [
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    re_path(r'^(?P<username>[\w.0+-]+)/', views.user_page, name='user_page')
]
