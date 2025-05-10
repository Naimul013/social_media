from django.urls import path
from . import views

app_name = 'social'
urlpatterns = [
    path('',views.home,name='home'),
    path('add_friend/',views.add_friend,name='add_friend'),
    path('add_friend/profile/<int:pk>/',views.profile,name='profile'),
    path('add_friend/user_profile/<int:pk>/',views.profile,name='user_profile'),
    path('follow/<int:pk>/',views.follow,name='follow'),
    path('unfollow/<int:pk>/',views.unfollow,name='unfollow'),
]
   
