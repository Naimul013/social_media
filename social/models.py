from django.db import models
from authentication.models import CustomUser
# Create your models here.
class Follow(models.Model):
    follower = models.ForeignKey(CustomUser, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(CustomUser, related_name='follower', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('follower','following')

class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField( upload_to='post_pic', height_field=None, width_field=None, max_length=None, blank= True, null=True)
    created_at = models.DateTimeField( auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True, blank=True, null=True)
    def __str__(self):
        return f"{self.author}'s post-{self.content[:20]}"
    
    def user_reacted(self, user):
        return self.reactions.filter(user=user).exists()
    
class React(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reactions')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ('user','post')

class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class Notification(models.Model):
    NOTIFICATION_TYPE = (
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow'),
    )
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="sent_notifications")
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='recieved_notifications')
    notification_type = models.CharField( max_length=10, choices=NOTIFICATION_TYPE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null= True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null= True)
    created_at = models.DateTimeField( auto_now_add=True)
    is_read = models.BooleanField(default=False)
    