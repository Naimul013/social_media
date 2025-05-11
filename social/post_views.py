from django.shortcuts import render,redirect,get_object_or_404
from .models import Post, Follow
from authentication.forms import PostForm


def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
        
            post.save()
            return redirect('social:home')
        
    else:
        form = PostForm()
    context = {'form':form}
    return render(request,'social/new_post.html',context)

def follow_user_list(request):
    following = Follow.objects.filter(follower= request.user)
    follower = Follow.objects.filter(following= request.user)
    print(follower)
    print(following)
    for i in following:
        print(i.following)
    
    following_user = request.GET.get('following_user') == 'true'
    if following_user:
        template = 'social/following_user.html'
    else:
        template = 'social/follower_user.html'
    context = {'following':following,'follower':follower}
    return render(request,template,context)