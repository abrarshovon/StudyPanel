from django.urls import path 
from . import views

urlpatterns = [
    path('',views.base, name ='base'),
    path('room/<str:pk>/',views.room, name ='room'),
    path('addroom/',views.addRoom, name ='addRoom'),
    path('updateroom/<str:pk>/',views.updateRoom, name ='updateRoom'),
    path('deleteroom/<str:pk>/',views.deleteRoom, name ='deleteRoom'),
    path('login/',views.signin, name='signin'),
    path('logout/',views.signout, name='signout'),
    path('signup/',views.signup, name='signup'),

    
]