from django.db import models
from django.contrib.auth.models import User 
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
"""
comment for models 
"""

class Album(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True)
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("photo:photo_albums", args=[self.slug])
    
    def save(self, *args, **kwargs):
        album_slug = (str(self.user) +'_'+ self.name)
        self.slug = slugify(album_slug)
        return super(Album, self).save(*args,**kwargs)

    
    
class Photo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, db_index=True)
    album = models.ForeignKey(Album,on_delete=models.SET_NULL, related_name ='photo', blank=True, null=True)
    title = models.CharField(max_length=200,blank = False, db_index=True)
    description = models.TextField(blank = True)
    image = models.ImageField(blank = False,upload_to = 'photo/%Y/%m/%d')
    slug = models.SlugField(max_length=200, unique=True)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("photo:detail", args=[self.id,self.slug])
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super(Photo, self).save(*args,**kwargs)
        

    