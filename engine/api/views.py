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

# create get all the waitlists
@api_view(['GET'])
def getWaitlisters(request):
    waitlist = Waitlist.objects.all()
    waitlistSerializer = WaitlistSerializer(waitlist, many=True)
    return Response(waitlistSerializer.data)

# save someone to waitlist
@api_view(['POST'])
def addToWaitlist(request):
    waitlistSerializer = WaitlistSerializer(data=request.data)
    if waitlistSerializer.is_valid():
        waitlistSerializer.save()
        return Response(waitlistSerializer.data, status=status.HTTP_201_CREATED)
    
# get specific waitlister
@api_view(['GET'])
def getWaitlister(request, pk):
    # try to get waitlist
    try:
        waitlister = Waitlist.objects.get(id=pk)
    except Waitlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    waitlistSerializer = WaitlistSerializer(waitlister, many=False)
    return Response(waitlistSerializer.data)

# update waitlister
@api_view(['PUT'])
def updateWaitlister(request, pk):
    # first, try to get waitlist
    try:
        waitlister = Waitlist.objects.get(id=pk)
    except Waitlist.DoesNotExist:
        # if not found, return 404
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # 
    waitlistSerializer = WaitlistSerializer(instance=waitlister, data=request.data)

    # check if data is valid
    if waitlistSerializer.is_valid():
        # if valid, save and return the updated data
        waitlistSerializer.save()
        return Response(waitlistSerializer.data)
    
    # if not valid, return 400
    return Response(status=status.HTTP_400_BAD_REQUEST)


# delete a waitlister
@api_view(['DELETE'])
def deleteWaitlister(request, pk):
    try:
        waitlister = Waitlist.objects.get(id=pk)
    except Waitlist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    waitlister.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)