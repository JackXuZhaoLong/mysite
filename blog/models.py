from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=20)
    blog_type = models.ForeignKey(BlogType,on_delete=models.DO_NOTHING)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    create_time = models.DateField(auto_now_add=True)
    last_updated_time = models.DateField(auto_now=True)
    def __str__(self):
        return "<Blog:%s>"% self.title
