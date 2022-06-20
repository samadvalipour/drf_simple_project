from rest_framework import serializers
from .models import Question,Answer

class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.SerializerMethodField()
    class Meta:
        model=Question
        fields = "__all__"
        extra_kwargs={
            "created":{'required':False},
            "user":{'required':False}
        }
    def get_answers(self,obj):
        ans = obj.answer.all()
        return AnswerSerializer(instance=ans,many=True).data


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields = "__all__"
    
