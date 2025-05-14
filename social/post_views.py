from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from authentication.forms import PostForm,CommentForm
from django.db.models import Q
from django.core.paginator import Paginator

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

def react(request,pk):
    post = get_object_or_404(Post,id= pk)
    reaction, created = React.objects.get_or_create(user = request.user, post= post)
    if not created:
        reaction.delete() #unlike
    if created:
        Notification.objects.create(
            sender = request.user,
            receiver = post.author,
            notification_type = 'like',
            post = post
        )
    return redirect('social:home')
    


def comment(request,pk):
    post = get_object_or_404(Post,id = pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            Notification.objects.create(
                sender = request.user,
                receiver = post.author,
                notification_type = 'comment',
                post = post
            )
            return redirect('social:home')
    else:
        form = CommentForm()


def edit_comment(request,pk,ck):
    post = get_object_or_404(Post,id= pk)
    comment = get_object_or_404(Comment,id = ck,user= request.user)

    
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('social:home')
    else:
        form = CommentForm(instance=comment)
    
    context = {'post':post, 'comment':comment,'form':form}
    return render(request,'social/edit_comments.html',context)


def delete_comment(request,pk):
    comment = get_object_or_404(Comment, id = pk)
    comment.delete()
    return redirect('social:home')


def notification_list(request):
    notifications = Notification.objects.filter(receiver = request.user).order_by('-created_at')
    
    notifications.filter(is_read = False).update(is_read = True)
    context = {'notifications':notifications}
    return render(request,'social/notifications.html',context)


def search(request):
    query = request.GET.get('q')
    posts = Post.objects.all()

    if query:
        posts =posts.filter(
            Q(content__icontains=query) |
            Q(author__username__icontains= query)
        )


    paginator = Paginator(posts,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj':page_obj, 'query':query}
    return render(request, 'social/search.html',context)