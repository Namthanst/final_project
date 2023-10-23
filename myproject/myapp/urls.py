from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('blog/', views.blog, name='blog'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
    path('blog5/', views.blog5, name='blog5'),
    path('blog10/', views.blog10, name='blog10'),
]