from django.urls import path
from .views import searchWithChatGPT

urlpatterns = [
    path('chatgpt/', searchWithChatGPT, name='chatgpt_search'),
]