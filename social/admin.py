from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Follow)
admin.site.register(Post)
admin.site.register(React)
admin.site.register(Comment)