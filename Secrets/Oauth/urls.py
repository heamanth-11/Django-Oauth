from django.urls import path
from . import views


urlpatterns = [
    path('home',views.api,name='getApi'),
 
]