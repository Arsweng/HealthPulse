from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Comment(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)