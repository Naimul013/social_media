from django.shortcuts import render,redirect,get_object_or_404
from authentication.models import CustomUser
from .models import Follow
# Create your views here.
def home(request):
    user = request.user
    follower = Follow.objects.filter(following = user)
    following = Follow.objects.filter(follower = user)
    context = {'user':user,'follower':follower, 'following':following}
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
    is_following = False
    if request.user.is_authenticated:
        is_following = Follow.objects.filter(follower=request.user, following=profile).exists()
    context = {'profile':profile,'is_following':is_following}

    return render(request,'social/profile.html',context)

def follow(request,pk):
    user_to_follow = get_object_or_404(CustomUser,id = pk)
    if user_to_follow != request.user:
        Follow.objects.get_or_create(follower = request.user, following = user_to_follow)
        
        
    return redirect('social:home')

def unfollow(request,pk):
    user_to_unfollow = get_object_or_404(CustomUser,id = pk)
    Follow.objects.filter(follower= request.user,following = user_to_unfollow).delete()
    return redirect('social:home')
    


