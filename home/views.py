from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Question,Answer
from .serializers import QuestionSerializer,AnswerSerializer
from rest_framework import status
class HomeView(APIView):
    def get(self,request):
        return Response({"msg":"Hello World"})

class QuestionCreateApi(APIView):
    def post(self,request):
        question_ser = QuestionSerializer(data=request.data)
        if question_ser.is_valid():
            Question.objects.create(
                user = request.user,
                body = question_ser.validated_data["body"],
                title = question_ser.validated_data["title"]
            )
            return Response({"msg":"question created"},status=status.HTTP_201_CREATED)
        return Response({"msg":"question creation faild"},status=status.HTTP_400_BAD_REQUEST)
        
class QuestionDeleteApi(APIView):
    def delete(self,request,pk):
        try:
            quetion = Question.objects.get(pk=pk)
            quetion.delete()
            return Response("question deleted",status=status.HTTP_200_OK)
        except:
            return Response("question deleting falid",status=status.HTTP_404_NOT_FOUND)

class QuestionUpdateApi(APIView):
    
    def put(self,request,pk):
        try:
            quetion = Question.objects.get(pk=pk)
            question_ser = QuestionSerializer(instance=quetion,data=request.data, partial=True)
            if question_ser.is_valid():
                question_ser.save()
                return Response("question updated",status=status.HTTP_200_OK)
            return Response("question updating faild",status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response("question updating falid",status=status.HTTP_404_NOT_FOUND)

class QuestionGetApi(APIView):
    def get(self,request,pk):
        try:
            question = Question.objects.get(pk=pk)
            question_ser = QuestionSerializer(instance=question)
            return Response(question_ser.data)
        except:
            return Response("question does not existe",status=status.HTTP_404_NOT_FOUND)

class QuestionsApi(APIView):
    def get(self,request):
        questions = Question.objects.all()
        questions_ser = QuestionSerializer(instance=questions,many=True)
        return Response(questions_ser.data)

    