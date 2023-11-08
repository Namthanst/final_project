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
    path('blog5/', views.blog5, name='blog5'),
    path('blog10/', views.blog10, name='blog10'),
    path('cpmixlink/', views.cpmixlink, name='cpmixlink'),
    path('cpmixlink/blog3', views.link, name='link'),
    path('cpmixlink/blog', views.link1, name='link1'),
    path('cpmixlink/blog2', views.link2, name='link2'),
    
    path('cpmixlink/blog4', views.link4, name='link4'),
    path('cpmixlink/blog6', views.link6, name='lin6'),
    path('cpmixlink/blog7', views.link7, name='link7'),
    path('cpmixlink/blog8', views.link8, name='link8'),
    path('cpmixlink/blog5', views.link5, name='link5'),
    path('cpmixlink/blog10', views.link10, name='link10'),
]