from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status

# register a new user
class RegisterView(GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user = serializer.data

            # send the user an email

            # respond with status
            return Response({
                'user': user,
                'message': 'Registration Successful'
            }, status=status.HTTP_201_CREATED)
        
        # if not valid, respond with errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
