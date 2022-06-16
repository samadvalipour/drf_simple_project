from rest_framework import serializers

class UserSerilaizer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True,write_only=True)
    email = serializers.EmailField(required=True)