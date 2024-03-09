from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('waitlists/', views.Waitlists.as_view()),
    path('waitlists/<int:pk>/', views.Waitlister.as_view()),
]