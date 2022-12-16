from django.http import HttpResponse
from django.shortcuts import render, redirect
from . forms import SigninForm, UserCreationForm, PhotoEditForm, PasswordChangeForm,PhotoUploadForm, AlbumCreationForm
from . models import Photo, Album   
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib import messages


# Create your views here.
@login_required()
def photo_list(request,album_slug=None,):
    user = request.user
    user_albums = Album.objects.filter(user=request.user)
    photos = Photo.objects.filter(user__username=request.user)
    if album_slug:
        album = get_object_or_404(Album,slug=album_slug)
        photos = photos.filter(album=album)
    context = {
        'photos': photos,
        'user_albums':user_albums,
        'user':user
    }
    return render(request,'photo_album/gallery.html',context)

@login_required()
def photo_detail(request,id,slug):
    photo = get_object_or_404(Photo,id=id,slug=slug)
    return render(request,'photo_album/detail.html',{'photo':photo})

def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request, "Signin Successful")
                return redirect('photo:photo_list')
                
            else:
                messages.error(request, "Issue Signing in, please look over your login credentials")
                return HttpResponse("Invalid Username or password")
                
    else:
        form = SigninForm()
        return render(request,'photo_album/signin.html',{'form':form})
    
@login_required()
def signout(request):
    logout(request)
    messages.success(request, "You've signed out sucessfully")
    return redirect('photo:signin')

def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            # create new user 
            new_user = user_form.save(commit=False)
            # set their password 
            new_user.set_password(cd['password'])
            new_user.username = cd['username']


            # setting default photo album 
            new_user.save()

            messages.success(request, "You're account was sucessfully created")
            return redirect('photo:signin')
    else:
        user_form = UserCreationForm()
        return render(request,'photo_album/register.html',{'user_form':user_form})
    
@login_required()
def edit(request,id,slug):
    photo = get_object_or_404(Photo,id=id,slug=slug)
    user = request.user 
    if request.method == 'POST':
        edit_form = PhotoEditForm(user,data=request.POST,files=request.FILES, instance=photo)
        if edit_form.is_valid():
            cd = edit_form.cleaned_data
            if cd['album']:
                photo.album = cd['album']
                photo.save()
            elif cd['new_album']:
                album = Album.objects.create(name=cd['new_album'],user=request.user)
                album.save()
                photo.album = album
                photo.save()
            edit_form.save()
            messages.success(request,"You're photo was sucessfully edited")
        return redirect('photo:photo_list')
    else:
        edit_form=PhotoEditForm(user, instance=photo)
        return render(request,'photo_album/edit.html',{'edit_form':edit_form,'photo':photo})
    
@login_required()
def password_change(request):
    if request.method == "POST":
        password_form = PasswordChangeForm(request.POST)
        if password_form.is_valid():
            cd = password_form.cleaned_data
            request.user.set_password(cd['password'])
            request.user.save()
            return redirect('photo:signin')
    else:
        password_form = PasswordChangeForm()
        return render(request,'photo_album/password_change.html',{'password_form':password_form})

@login_required()    
def upload(request):
    user = request.user 
    if request.method == "POST":
        upload_form = PhotoUploadForm(user, data=request.POST, files=request.FILES)
        if upload_form.is_valid():
            cd = upload_form.cleaned_data
            if cd['new_album']:
                album = Album.objects.create(name=cd['new_album'],user=user)
                album.save()
                new_photo = Photo.objects.create(user=user,title=cd['title'],description=cd['description'],image=cd['image'],album=album)
            elif cd['album']:
                album = Album.objects.get(name=cd['album'])
                new_photo = Photo.objects.create(user=user,title=cd['title'],description=cd['description'],image=cd['image'],album=album)
            else:
                new_photo = Photo.objects.create(user=user,title=cd['title'],description=cd['description'],image=cd['image'])

            new_photo.save()
            messages.success(request,'Your photo was sucessfully uploaded')
            return redirect('photo:photo_list')
        else:
            messages.error(request,'one of the fields were invalid')
            return redirect('photo:upload')
    else:
        upload_form = PhotoUploadForm(user)
        return render(request,'photo_album/upload.html',{'upload_form':upload_form})

@login_required()
def photo_delete(request,id):
    photo = get_object_or_404(Photo,id=id)
    if request.method == "POST":
        photo.delete()
        messages.success(request, "Your Photo was sucessfully Deleted")
        return redirect("photo:photo_list")
    else:
        return render(request,"photo_album/photo_delete.html")

@login_required
def album_delete(request,id):
    album = get_object_or_404(Album,id=id)
    if request.method == "POST":
        album.delete()
        messages.success(request,"The album " +album.name+" was deleted successfully")
        return redirect("photo:photo_list")
    else:
        return render(request,"photo_album/album_delete.html")

@login_required
def album_create(request):
    if request.method =="POST":
        album_form = AlbumCreationForm(request.POST)
        if album_form.is_valid():
            cd = album_form.cleaned_data
            album = Album.objects.create(name=cd["name"],user=request.user)
            album.save()
            messages.success(request,"Your album was successfully created")
            return redirect("photo:photo_list")
    else:
        album_form = AlbumCreationForm()
    return render(request,'photo_album/album_create.html',{'album_form':album_form})


    