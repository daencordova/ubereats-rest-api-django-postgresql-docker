from rest_framework import generics, permissions

from .serializers import UserSerializer


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
