from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return JsonResponse({
        "message": "We're alive! Let's change the world!!"
    })