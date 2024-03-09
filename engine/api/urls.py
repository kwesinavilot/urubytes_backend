from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('waitlists/', views.getWaitlist, name='getwaitlists'),
    path('waitlists/add', views.addToWaitlist, name='savewaitlist'),
    # path('contact/', views.saveContact, name='savecontact'),
    # path('admin/', admin.site.urls),
]