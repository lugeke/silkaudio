from rest_framework import viewsets, permissions, generics
from knox.auth import TokenAuthentication
from rest_framework.authentication import SessionAuthentication
from rest_framework import mixins

from audiobooks.models import Audiobook, Author, History
from audiobooks.serializers import \
    AudiobookSerializer, AuthorSerializer, HistorySerializer
from silkaudio.permissions import\
    HasReadOrStaffPermission, IsOwner
from silkaudio.put_as_create import AllowPUTAsCreateMixin


class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = Audiobook.objects.all()
    serializer_class = AudiobookSerializer
    permission_classes = (HasReadOrStaffPermission,)


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (HasReadOrStaffPermission,)


# class HistoryViewSet(viewsets.ModelViewSet):
#     serializer_class = HistorySerializer
#     authentication_classes = (TokenAuthentication, SessionAuthentication)
#     permission_classes = (permissions.IsAuthenticated, IsOwner)

#     def get_queryset(self):
#         return History.objects.filter(user=self.request.user)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)

class HistoryView(AllowPUTAsCreateMixin,
                  mixins.ListModelMixin,
                  generics.GenericAPIView):
    serializer_class = HistorySerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated, IsOwner)

    def get_queryset(self):
        return History.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        print(request.data['audiobook'])
        print(args)
        print(kwargs)
        return self.update(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """ 
        queryset = self.filter_queryset(self.get_queryset())

        obj = generics.get_object_or_404(queryset, audiobook=self.request.data['audiobook'])

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj
