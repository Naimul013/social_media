from django.urls import path
from . import views
from . import post_views

app_name = 'social'
urlpatterns = [
    path('',views.home,name='home'),
    path('add_friend/',views.add_friend,name='add_friend'),
    path('add_friend/profile/<int:pk>/',views.profile,name='profile'),
    path('add_friend/user_profile/<int:pk>/',views.profile,name='user_profile'),
    path('follow/<int:pk>/',views.follow,name='follow'),
    path('unfollow/<int:pk>/',views.unfollow,name='unfollow'),
    path('profile_edit/<int:pk>/',views.profile_edit,name='profile_edit'),
    path('new_post/',post_views.new_post,name='new_post'),
    path('following_users/',post_views.follow_user_list,name='following_users'),
    path('follower_users/',post_views.follow_user_list,name='follower_users'),

]
   
