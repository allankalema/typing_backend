from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import TextPassage, TypingSession
from .serializers import TextPassageSerializer, TypingSessionSerializer, UserProgressSerializer
from accounts.models import CustomUser

class TextPassageList(generics.ListAPIView):
    queryset = TextPassage.objects.all()
    serializer_class = TextPassageSerializer
    permission_classes = [permissions.AllowAny]

class TypingSessionCreate(generics.CreateAPIView):
    queryset = TypingSession.objects.all()
    serializer_class = TypingSessionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(user=self.request.user)
        else:
            serializer.save()

class UserProgressView(generics.RetrieveAPIView):
    serializer_class = UserProgressSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user