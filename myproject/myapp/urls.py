from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('blog/', views.blog, name='blog'),
    path('blog2/', views.blog2, name='blog2'),
    path('blog3/', views.blog3, name='blog3'),
    path('blog4/', views.blog4, name='blog4'),
    path('blog6/', views.blog6, name='blog6'),
    path('blog7/', views.blog7, name='blog7'),
    path('blog8/', views.blog8, name='blog8'),
]