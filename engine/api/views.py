from django.http import Http404, JsonResponse
from .models import Waitlist
from .serializers import WaitlistSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
@api_view(['GET'])
def index(request):
    return JsonResponse({
        "message": "We're alive! Let's change the world!!"
    })

# list all the waitlisters or create a new one
class Waitlists(APIView): 
    # create get all the waitlists
    def get(self, request, format=None):
        waitlist = Waitlist.objects.all()
        waitlistSerializer = WaitlistSerializer(waitlist, many=True)
        return Response(waitlistSerializer.data)

    # add someone to waitlist
    def post(self, request, format=None):
        waitlistSerializer = WaitlistSerializer(data=request.data)

        if waitlistSerializer.is_valid():
            waitlistSerializer.save()
            return Response(waitlistSerializer.data, status=status.HTTP_201_CREATED)
        
        return Response(waitlistSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# Retrieve, update or delete a waitlister
class Waitlister(APIView):
    # get specific waitlister
    def getWaitlister(self, pk):
        # try to get waitlist
        try:
            return Waitlist.objects.get(id=pk)
        except Waitlist.DoesNotExist:
            # if not found, return 404
            raise Http404
    
    # get and return specific waitlister
    def get(self, request, pk, format=None):
        waitlister = self.getWaitlister(pk)
        waitlistSerializer = WaitlistSerializer(waitlister, many=False)
        return Response(waitlistSerializer.data)

    # update waitlister
    def put(self, request, pk, format=None):
        waitlister = self.getWaitlister(pk)
        
        waitlistSerializer = WaitlistSerializer(instance=waitlister, data=request.data)

        # check if data is valid
        if waitlistSerializer.is_valid():
            # if valid, save and return the updated data
            waitlistSerializer.save()
            return Response(waitlistSerializer.data)
        
        # if not valid, return 400
        return Response(status=status.HTTP_400_BAD_REQUEST)

    # delete a waitlister
    def delete(self, request, pk, format=None):
        waitlister = self.getWaitlister(pk)
        waitlister.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)