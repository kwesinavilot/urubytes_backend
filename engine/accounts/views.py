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
    # collect inputs for user
    name = request.data.get('name')
    email = request.data.get('email')
    password = request.data.get('password')

    # collect inputs for organization
    industry = request.data.get('industry')
    organization = request.data.get('organization')
    size = request.data.get('size')
    role = request.data.get('role')
    country = request.data.get('country')

    # collect inputs for insights
    interests = request.data.get('interests')
    referrer = request.data.get('referrer')

    # validate inputs
    required_fields = ['name', 'email', 'password', 'industry', 'organization', 'size', 'role', 'country', 'interests', 'referrer']
    error_message = [field for field in required_fields if not request.data.get(field)]

    # respond with bag of errors
    if error_message:
        return Response({'error': f'Missing required fields: {", ".join(error_message)}'}, status=status.HTTP_400_BAD_REQUEST)

    orgID = generateOrgID()
    userID = generateUserID()

    # orgSerializer = OrganizationSerializer(data={'orgID': orgID, 'industry': industry, 'name': organization, 'size': size, 'country': country})
    # userSerializer = UserSerializer(data={'userID': userID, 'orgID': orgID, 'name': name, 'email': email, 'role': role, 'password': password})
    # insightsSerializer = InsightSerializer(data={'userID': userID, 'interests': interests, 'referrer': referrer})

    # # Validate serializers
    # if not all([userSerializer.is_valid(), orgSerializer.is_valid(), insightsSerializer.is_valid()]):
    #     return Response({
    #         'error': 'Invalid data',
    #         'user_errors': userSerializer.errors,
    #         'org_errors': orgSerializer.errors,
    #         'insights_errors': insightsSerializer.errors
    #     }, status=status.HTTP_400_BAD_REQUEST)

    # # Save user, organization, and insights
    # organization = orgSerializer.save()
    # user = userSerializer.save()
    # insights = insightsSerializer.save()

    
    # Create organization instance
    organization = Organization.objects.create(
        orgID=generateOrgID(), 
        name=organization,
        industry=industry, 
        size=size, 
        country=country
    )

    # Create user instance
    user = User.objects.create(
        userID=generateUserID(),
        orgID=organization,
        name=name, 
        email=email, 
        role=role, 
        password=password
    )

    # Create insights instance
    insights = Insight.objects.create(
        userID=user,
        interests=interests,
        referrer=referrer
    )

    # try:
    #     # Create organization instance
    #     organization = Organization.objects.create(
    #         orgID=generateOrgID(), 
    #         name=organization,
    #         industry=industry, 
    #         size=size, 
    #         country=country
    #     )

    #     # Create user instance
    #     user = User.objects.create(
    #         userID=generateUserID(),
    #         orgID=organization,
    #         name=name, 
    #         email=email, 
    #         role=role, 
    #         password=password
    #     )

    #     # Create insights instance
    #     insights = Insight.objects.create(
    #         userID=user,
    #         interests=interests,
    #         referrer=referrer
    #     )
    # except Exception as e:
    #     return Response({'error': f'Failed to create user: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

    return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)








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
