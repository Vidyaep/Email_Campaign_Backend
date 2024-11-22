from rest_framework import serializers
from .models import Campaign, User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class CampaignSerializer(serializers.ModelSerializer):
    recipients = UserSerializer(many=True)

    class Meta:
        model = Campaign
        fields = '__all__'

class CampaignCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
