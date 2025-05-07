from rest_framework import serializers
from .models import TextPassage, TypingSession
from accounts.models import CustomUser

class TextPassageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextPassage
        fields = ['id', 'content', 'difficulty']

class TypingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypingSession
        fields = ['id', 'passage', 'wpm', 'accuracy', 'errors', 'time_taken', 'date_completed']
        read_only_fields = ['user']

class UserProgressSerializer(serializers.ModelSerializer):
    typing_sessions = TypingSessionSerializer(many=True, read_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'typing_speed_goal', 'typing_sessions']