from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from datetime import datetime 

class Post(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=70)
    desc=models.TextField()
    feild=models.CharField(max_length=40)
    datetime=models.DateField(default=datetime.now)


    

    # def__str__(self):)
    #     return self.title + 'by' + self.author


class BlogComment(models.Model):
    sn=models.AutoField(primary_key=True)
    body=models.TextField(max_length=1000)
    name=models.TextField(max_length=100)
    # user=models.ForeignKey(User,on_delete=models.CASCADE)
    posts=models.ForeignKey(Post,related_name='commentt',on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    # def__str(self):
    #     return '%s - %s' % (self.post.title, self.name)
