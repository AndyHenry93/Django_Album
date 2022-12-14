from django import forms
from django.contrib.auth.models import User 
from . models import Photo,Album

class SigninForm(forms.Form):
    username = forms.CharField(max_length=200,required=True)
    password = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput)

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(max_length=200,required=True)
    password = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput,)
    password2 = forms.CharField(max_length=20,required=True,widget=forms.PasswordInput,label="confirm password")

    class Meta:
        model = User
        fields = ('first_name','last_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("The passwords didn't match")

class PhotoEditForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), label="Album",required=False)
    new_album = forms.CharField(max_length=100,label="Create Album",required=False)
    def __init__(self,user,*args,**kwargs):
        super(PhotoEditForm,self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(user = user)
    
    class Meta:
        model = Photo
        fields = ('title','description','image',)
        
class PasswordChangeForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput,label="New Password")
    password_2 = forms.CharField(widget=forms.PasswordInput, label="Comfirm Password")

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            return forms.ValidationError("The Passwords didn't match")
        
class PhotoUploadForm(forms.ModelForm):
    album = forms.ModelChoiceField(queryset=Album.objects.all(), label="My Albums",required=False) 
    new_album = forms.CharField(max_length=100,label="Create Album",required=False)
    def __init__(self,user,*args,**kwargs):
        super(PhotoUploadForm,self).__init__(*args, **kwargs)
        self.fields['album'].queryset = Album.objects.filter(photo__user = user).distinct()
        
    class Meta:
        model = Photo
        fields = ('title','description','image')

class AlbumCreationForm(forms.Form):
    name = forms.CharField(max_length=50,required=True,label="Name")

