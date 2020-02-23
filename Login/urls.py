from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serializers, viewsets
from Login.views import CustomAuthToken

from Login import views

urlpatterns = [
    re_path(r'login/$', CustomAuthToken.as_view()),
    re_path(r'example2_list/$',views.Example2List.as_view()),
    #re_path(r'example2_detail/(?P<id>\d+)/$',views.Example2Detail.as_view())
    #Hola soy RockLee444
]