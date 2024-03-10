from rest_framework import serializers
from .models import User, Organization, Insight


#     def validate(self, attrs):
#         if User.objects.filter(email=attrs['email']).exists():
#             raise serializers.ValidationError({'email': 'Email already in use'})
        
#         return attrs


# create a user serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['userID', 'orgID','name', 'email', 'role', 'password']

# create serializer for organizations
class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['orgID', 'industry', 'name', 'size', 'country']

# create serializer for insights
class InsightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insight
        fields = ['user', 'interests', 'referrer']