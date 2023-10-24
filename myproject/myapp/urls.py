from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('blog/', views.blog, name='blog'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
<<<<<<< HEAD
    path('blog4/', views.blog4, name='blog4'),
    path('blog6/', views.blog6, name='blog6'),
    path('blog7/', views.blog7, name='blog7'),
    path('blog8/', views.blog8, name='blog8'),
=======
    path('blog5/', views.blog5, name='blog5'),
    path('blog10/', views.blog10, name='blog10'),
>>>>>>> 4a34b60d24aa70bcad05e8bc5fb72adb0e8f3add
]