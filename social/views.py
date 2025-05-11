from django.shortcuts import render,redirect,get_object_or_404
from authentication.models import CustomUser
from .models import Follow
from authentication.forms import *
from django.http import HttpResponseForbidden
# Create your views here.
def home(request):
    user = request.user
    follower = Follow.objects.filter(following = user)
    following = Follow.objects.filter(follower = user)

    following_only = request.GET.get('following_only') == 'true'
    if following_only and request.user.is_authenticated:
        following_users = request.user.following.values_list('following',flat = True)
        post = Post.objects.filter(author__in = following_users)
    else: 
        post = Post.objects.all()

    context = {'user':user,'follower':follower, 'following':following,'post':post}
    return render(request,'social/home.html',context)

def add_friend(request):
    member = CustomUser.objects.all()
    for members in member:
        print(members.username)
    print(request.user.username)
    context = {'member':member}
    return render(request,'social/add_friend.html',context)

def profile(request,pk):
    profile = get_object_or_404(CustomUser,id=pk)
    post = Post.objects.filter(author = profile)
    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(follower=request.user, following=profile).exists()

    if profile == request.user:
        template = 'social/user_profile.html'
    else:
        template = 'social/profile.html'
    
    context = {'profile':profile,'is_following':is_following,'posts':post}

    return render(request,template,context)

def follow(request,pk):
    user_to_follow = get_object_or_404(CustomUser,id = pk)
    if user_to_follow != request.user:
        Follow.objects.get_or_create(follower = request.user, following = user_to_follow)
        
        
    return redirect('social:home')

def unfollow(request,pk):
    user_to_unfollow = get_object_or_404(CustomUser,id = pk)
    Follow.objects.filter(follower= request.user,following = user_to_unfollow).delete()
    return redirect('social:home')
    


def profile_edit(request,pk):
    previos_data = get_object_or_404(CustomUser,id=pk)
    if request.user.id != previos_data.id:
        return HttpResponseForbidden('You are not allowed to change that')

    if request.method == "POST":
        form = EditProfileForm(request.POST,request.FILES,instance = previos_data)
        if form.is_valid():
            
            form.save()
            return redirect('social:user_profile',pk=pk)
    else:
        form = EditProfileForm(instance = previos_data)
    context = {'form':form}
    return render(request,'social/profile_edit.html',context)
