from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
        path('',views.index, name="index" ),
        path('about',views.about, name="about" ),
        path('blog',views.blog, name="blog" ),
        path('contact',views.contact, name="contact" ),
        path('coffee',views.coffee, name="coffee" ),
        path('signup',views.signup, name="signup" ),
]
