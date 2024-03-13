from rest_framework import serializers
from .models import User, Organization, Insight

# create a user serializer
class UserSerializer(serializers.ModelSerializer):
    userID = serializers.CharField(read_only=True)
    orgID = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())
    name = serializers.CharField()
    email = serializers.EmailField()
    role = serializers.CharField()
    # password = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_length=8)

    class Meta:
        model = User
        fields = ['userID', 'orgID','name', 'email', 'role']

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