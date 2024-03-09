from django.http import JsonResponse
from django.shortcuts import render
from .models import Waitlist
from .serializers import WaitlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def index(request):
    return JsonResponse({
        "message": "We're alive! Let's change the world!!"
    })

# create get endpoint for waitlist
@api_view(['GET'])
def getWaitlist(request):
    waitlist = Waitlist.objects.all()
    waitlistSerializer = WaitlistSerializer(waitlist, many=True)
    return JsonResponse({"waitlist" : waitlistSerializer.data})

# create post/save endpoint for waitlist
@api_view(['POST'])
def addToWaitlist(request):
    waitlistSerializer = WaitlistSerializer(data=request.data)
    if waitlistSerializer.is_valid():
        waitlistSerializer.save()
        return Response(waitlistSerializer.data, status=status.HTTP_201_CREATED)