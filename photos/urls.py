from django.urls import path
from . import views

app_name = "photo"

urlpatterns = [
    path('',views.photo_list,name="photo_list"),
    path('album/<slug:album_slug>/',views.photo_list,name='photo_albums'),
    path('signin/',views.signin,name='signin'),
    path('signout/',views.signout,name='signout'),
    path('register_done/',views.register,name='register_done'),
    path('register/',views.register,name='register'),
    path('photo/<int:id>/<str:slug>/',views.photo_detail,name='detail'),
    path('edit/<int:id>/<str:slug>/',views.edit,name='edit'),
    path('password_change/',views.password_change,name='password_change'),
    path('upload/',views.upload,name='upload'),
    path('delete/<int:id>/',views.delete,name="delete"),
]
