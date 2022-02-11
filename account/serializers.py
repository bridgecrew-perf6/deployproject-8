from rest_framework import serializers
from .models import *
from .utils import send_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=4, required=True, write_only=True)
    password_confirm = serializers.CharField(min_length=4, required=True, write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "password_confirm")

    def validate(self, data):
        password = data.get('password')
        password_confirm = data.pop("password_confirm")
        if password != password_confirm:
            msg = ("Пароли не совпадают")
            raise serializers.ValidationError(msg)
        return data

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


