from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<int:id>', views.database, name='database'),
    path('service', views.service, name='service'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'), 
    path('contactUs', views.contactUs, name='contactUs'),
    path('home', views.home, name='home'),
    path('insertDetails', views.insertContactDetails, name='insertDetails'),
    path('insertEmail', views.newsTellerSub, name='newsTeller'),
]