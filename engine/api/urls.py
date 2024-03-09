from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('waitlists/', views.getWaitlisters, name='getWaitlisters'),
    path('waitlists/add', views.addToWaitlist, name='addWaitlister'),
    path('waitlists/<int:pk>', views.getWaitlister, name='getWaitlister'),
    path('waitlists/<int:pk>/update', views.updateWaitlister, name='updateWaitlister'),
    path('waitlists/<int:pk>/delete', views.deleteWaitlister, name='deleteWaitlister'),
    # path('contact/', views.saveContact, name='savecontact'),
    # path('admin/', admin.site.urls),
]