from django.http import JsonResponse
from django.shortcuts import render
from .models import Waitlist
from .serializers import WaitlistSerializer

# Create your views here.
def index(request):
    return JsonResponse({
        "message": "We're alive! Let's change the world!!"
    })

# create get endpoint for waitlist
def getWaitlist(request):
    waitlist = Waitlist.objects.all()
    print(waitlist)
    waitlistSerializer = WaitlistSerializer(waitlist, many=True)
    return JsonResponse({"waitlist" : waitlistSerializer.data}, safe=False)