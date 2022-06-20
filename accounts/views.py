from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serilaizers import UserSerilaizer
from rest_framework import status,permissions,authentication


class UserRegitrations(APIView):
    def post(self,request):
        user_data = request.data
        user_ser = UserSerilaizer(data=user_data)
        if user_ser.is_valid():
            User.objects.create_user(
                username = user_ser.validated_data["username"],
                email = user_ser.validated_data["email"],
                password = user_ser.validated_data["password"]
            )
            return Response({'msg':"Registration is successful"},status=status.HTTP_201_CREATED)
        return Response(user_ser.errors,status=status.HTTP_400_BAD_REQUEST)

class GetAllUsers(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self,request):
        users = User.objects.all()
        user_ser = UserSerilaizer(instance=users,many=True)
        return Response(user_ser.data)