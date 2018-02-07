from rest_framework import serializers
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username')


class UserRegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'username')

    def create(self, validated_data):
        """
        Create the object.
        :param validated_data: string
        """
        user = User(email=validated_data['email'],
                    username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, value):
        """
        Validate if email is valid or there is an user using the email.
        :param value: string
        :return: string
        """

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError('''Email already in use,' \
            please use a different email address.''')

        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('Username already in use')
        return value
