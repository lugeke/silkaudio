from rest_framework import serializers
from audiobooks.models import Audiobook, Author, History, User


class AudiobookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audiobook
        fields = ('id', 'title', 'authors', 'chapters', 'description')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ('id', 'audiobook', 'progress', 'recentListen')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', )
