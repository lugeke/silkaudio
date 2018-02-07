from rest_framework import permissions
from knox.models import AuthToken
from rest_framework.authentication import\
  BasicAuthentication, SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from knox.auth import TokenAuthentication

from accounts.serializers import UserSerializer, UserRegistrationSerializer


class UserView(GenericAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        return Response(self.get_serializer(request.user).data)


class UserRegisterView(CreateModelMixin, GenericAPIView):
    serializer_class = UserRegistrationSerializer
    authentication_classes = ()

    def post(self, request):
        """User registration view."""
        return self.create(request)


class UserLoginView(GenericAPIView):
    serializer_class = UserSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        """User login with username and password."""
        token = AuthToken.objects.create(request.user)
        data = self.get_serializer(request.user).data
        return Response({
            **data,
            'token': token,
        })
