from rest_framework import serializers

from .models import Post, SignIn, TwoFA


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'username', 'password', 'ip'
        )


class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = (
            'error', 'messages', 'value', 'question', 'twoFA'
        )


class TwoFASerializer(serializers.ModelSerializer):
    class Meta:
        model = TwoFA
        fields = (
            'twoFaType', 'gaActivated'
        )
