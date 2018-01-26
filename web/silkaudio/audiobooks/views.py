from audiobooks.models import Audiobook, Author, History, User
from audiobooks.serializers import \
    AudiobookSerializer, AuthorSerializer, HistorySerializer, UserSerializer
from rest_framework import viewsets, permissions
from audiobooks.permissions import HasReadOrStaffPermission, IsOwnerOrReadOnly


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
    permission_classes = (permissions.IsAdminUser,)


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)
