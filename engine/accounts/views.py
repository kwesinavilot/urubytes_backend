from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegistrationSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

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

# class ObtainUserPairSerializer(TokenObtainPairSerializer):
#     @classmethod
#     def get_token(cls, user):
#         token = super().get_token(user)

#         # Add custom claims
#         # get user's name through serializer
#         serializer = UserSerializer(user)
#         # token['email'] = user.email
#         token['name'] = serializer.data['name']
#         return token
#         return token
