"""RecommenderSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('Book_Recommender_System_App.urls')),
    path('admin/', admin.site.urls),
]
