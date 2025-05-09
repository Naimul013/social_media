from django.urls import path
from . import views

app_name = 'authentication'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.handlelogin,name='login'),
    path('logout/',views.handlelogout,name='logout')
]

