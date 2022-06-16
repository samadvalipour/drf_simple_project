from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serilaizers import UserSerilaizer

class UserRegitrations(APIView):
    def post(self,request):
        user_data = request.data
        user_ser = UserSerilaizer(data=user_data)
        if user_ser.is_valid():
            User.objects.create(
                username = user_ser.validated_data["username"],
                email = user_ser.validated_data["email"],
                password = user_ser.validated_data["password"]
            )
            return Response({'msg':"Registration is successful"})
        return Response(user_ser.errors)

class GetAllUsers(APIView):
    def get(self,request):
        users = User.objects.all()
        user_ser = UserSerilaizer(instance=users,many=True)
        return Response(user_ser.data)