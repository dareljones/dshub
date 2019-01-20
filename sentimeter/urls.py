from django.conf.urls import url
from django.urls import path,include

from . import views
from .views import userinput

urlpatterns = [
    path('', views.index, name='index'),
    path('sentianalyse/',views.analyse,name='analyse'),
]