from django.http import JsonResponse
from .models import Waitlist, Contact
from .serializers import WaitlistSerializer, ContactSerializer
from rest_framework.decorators import api_view
from rest_framework import generics, mixins

# Create your views here.
@api_view(['GET'])
def index(request):
    return JsonResponse({
        "message": "We're alive! Let's change the world!!"
    })

# list all the waitlisters or create a new one
class Waitlists(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): 
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer

    # get all the waitlists
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # add someone to waitlist
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve, update or delete a waitlister
class Waitlister(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Waitlist.objects.all()
    serializer_class = WaitlistSerializer
    
    # get and return specific waitlister
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # update waitlister
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # delete a waitlister
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# list all the contacts or create a new one
class Contacts(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): 
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    # get all the contacts
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # add new contact
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

# Retrieve, update or delete a contact
class Contacter(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    # get and return specific contact
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    # update contact
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    # delete a contact
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)