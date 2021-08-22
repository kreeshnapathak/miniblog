from django.contrib import admin
from .models import BlogComment, Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=('id','title','author','desc','feild','datetime')


@admin.register(BlogComment)
class PostAdmin(admin.ModelAdmin):
    list_display=('sn','body','name','posts','parent','timestamp')


    
