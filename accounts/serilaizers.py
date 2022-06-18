from django.forms import CharField
from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        extra_kwargs = {
            "password":{"write_only":True}
        }

    def validate_username(self,value):
        if value == "admin":
            raise serializers.ValidationError("username should not be 'admin'")
        return value