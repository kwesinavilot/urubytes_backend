from rest_framework import serializers
from .models import User, Organization, Insight

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True, min_lenth=8)
    
    class Meta:
        model = User
        fields = '__all__'

    def validate(self, attrs):
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email': 'Email already in use'})
        
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)