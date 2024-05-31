from django.urls import path
from . import views

urlpatterns = [

    path('',views.home, name = "homeview"),
    path('room/',views.room,name = 'roomview'),
    path('get_token/',views.getToken),
    path('create_member/',views.createmember),
    path('get_member/',views.getmember),
    path('get_delete/', views.deletemember),

]