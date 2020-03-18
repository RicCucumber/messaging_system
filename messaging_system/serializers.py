from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message


class MessageCreateSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.username')

    class Meta:
        model = Message
        exclude = ['message_status']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'
