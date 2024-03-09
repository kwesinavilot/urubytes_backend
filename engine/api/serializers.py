from rest_framework import serializers
from .models import Waitlist, Contact

class WaitlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waitlist
        fields = '__all__'