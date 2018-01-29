from audiobooks.models import Audiobook, Author, History, User
from audiobooks.serializers import \
    AudiobookSerializer, AuthorSerializer, HistorySerializer, UserSerializer
from rest_framework import viewsets, permissions
from audiobooks.permissions import\
    HasReadOrStaffPermission, IsOwner


class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
    permission_classes = (HasReadOrStaffPermission,)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (HasReadOrStaffPermission,)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action in ['list', 'create', 'destroy']:
            permission_classes = [permissions.IsAdminUser]
        elif self.action in ['retrieve']:
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [IsOwner]
        return [p() for p in permission_classes]


class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        return History.objects.filter(user=self.request.user).all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

