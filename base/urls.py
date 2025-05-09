from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.loginUser,name='login'),
    path('register/',views.registerPage,name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('',views.home , name="home"),
    path("room/<str:pk>/", views.room, name="room"),
    path("create-room/",views.create_room,name = "create-room"),
    path("update-room/<str:pk>/", views.Update_room, name="update-room"),
    path('delete-room/<str:pk>',views.deleteRoom,name='delete_room'),
    path('delete-message/<int:pk>/', views.deleteMessage, name='delete-message'),
    path('profile/<str:pk>/',views.profile,name='profile'),
    path('update-user/',views.updateUser,name='update-user'),

  
] 
