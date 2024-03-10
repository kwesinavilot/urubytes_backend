from .serializers import UserSerializer, OrganizationSerializer, InsightSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view
from .models import User, Organization, Insight
from .utils import generateOrgID, generateUserID
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework import views
from rest_framework_simplejwt.tokens import RefreshToken

# register a new user
@api_view(['POST'])
def registerUser(request):
    required_fields = ['name', 'email', 'password', 'industry', 'organization', 'size', 'role', 'country', 'interests', 'referrer']

    # Validate required fields using list comprehension
    missing_fields = [field for field in required_fields if field not in request.data]
    if missing_fields:
        return Response({'error': f'Missing required fields: {", ".join(missing_fields)}'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Additional validation for password length
    try:
        validate_password(request.data['password'])
    except ValidationError as e:
        return Response({'error': f'Invalid password: {e}'}, status=status.HTTP_400_BAD_REQUEST)

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
            orgID=organization,  # Link to created organization
        )

        user.set_password(request.data['password'])
        user.save()

        # Create insight with user foreign key
        Insight.objects.create(
            userID=user,
            interests=request.data['interests'],
            referrer=request.data['referrer'],
        )

        # Log the user in
        login(request, user)

        # Generate JWT token for the user
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # Return token and user details in response
        return Response({
            'message': 'User registered and logged in successfully',
            'user': UserSerializer(user).data,
            'token': token
        }, status=status.HTTP_201_CREATED)

    except Exception as e:
        return Response({'error': f'Failed to create user: {str(e)}'}, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView():
    def post(self, request):
        # Extract email and password from request data
        email = request.data.get('email')
        password = request.data.get('password')

        # Authenticate user
        user = authenticate(email=email, password=password)

        if user:
            # Generate JWT token
            refresh = RefreshToken.for_user(user)
            token = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }

            # Login user
            login(request, user)

            # Return token in response
            return Response(token, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        # ...

        return token