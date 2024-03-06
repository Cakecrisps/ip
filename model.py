from django.db import models

# Create your models here.
class PostCategory(models.Model):
    name = models.CharField(max_length=32)
    views_count = models.IntegerField()
    def __str__(self):
        return self.name
class Post(models.Model):
    author = models.CharField(max_length=64)
    desc = models.TextField(null= True,blank=True,max_length=128)
    img = models.ImageField(upload_to='posts_imgs')
    content = models.TextField()
    categoryes = models.TextField()
    def __str__(self):
        return self.desc
#class User(models.Model):
#    username = models.CharField(max_length=64)
#    about = models.TextField()
#    login = models.TextField()
#   password = models.TextField()
#    views = models.IntegerField()
