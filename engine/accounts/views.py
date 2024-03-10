from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializer, OrganizationSerializer, InsightSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from .models import User, Organization, Insight
from .utils import generateOrgID, generateUserID

# register a new user
@api_view(['POST'])
def registerUser(request):
    required_fields = ['name', 'email', 'password', 'industry', 'organization', 'size', 'role', 'country', 'interests', 'referrer']

    # Validate required fields using list comprehension
    missing_fields = [field for field in required_fields if field not in request.data]
    if missing_fields:
        return Response({'error': f'Missing required fields: {", ".join(missing_fields)}'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        # Create organization
        organization = Organization.objects.create(
            orgID=generateOrgID(),
            name=request.data['organization'],
            industry=request.data['industry'],
            size=request.data['size'],
            country=request.data['country'],
        )

        # Create user with organization foreign key
        user = User.objects.create(
            userID=generateUserID(),
            name=request.data['name'],
            email=request.data['email'],
            role=request.data['role'],
            password=request.data['password'],
            orgID=organization,  # Link to created organization
        )

        # Create insight with user foreign key
        Insight.objects.create(
            userID=user,
            interests=request.data['interests'],
            referrer=request.data['referrer'],
        )

        #Consider returning serialized user data instead of a generic message
        return Response({
            'message': 'User registered successfully',
            # 'user': userSerializer.data,
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': f'Failed to create user: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)








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
