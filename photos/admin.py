from django.contrib import admin
from . models import Photo, Album
# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','slug','image','user','album')
    prepopulated_fields = {'slug':('title',)}
    
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name','slug','user')
    prepopulated_fields = {'slug':('name','user')}