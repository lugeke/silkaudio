from audiobooks.models import Audiobook, Author, History, User
from audiobooks.serializers import \
    AudiobookSerializer, AuthorSerializer, HistorySerializer, UserSerializer
from rest_framework import viewsets, permissions
from audiobooks.permissions import HasReadOrStaffPermission, IsOwner, HistoryPermission


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
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)
    
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
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner, HistoryPermission)

    # def get_permissions(self):
    #     if self.action 

    def get_queryset(self):
        return History.objects.filter(user=self.request.user).all()
