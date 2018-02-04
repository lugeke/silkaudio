from audiobooks.models import Audiobook, Author, History
from audiobooks.serializers import \
    AudiobookSerializer, AuthorSerializer, HistorySerializer
from rest_framework import viewsets, permissions
from silkaudio.permissions import\
    HasReadOrStaffPermission, IsOwner
from knox.auth import TokenAuthentication


class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
    permission_classes = (HasReadOrStaffPermission,)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (HasReadOrStaffPermission,)


class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        return History.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
