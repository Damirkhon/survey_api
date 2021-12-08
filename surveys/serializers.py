from rest_framework import serializers
from rest_framework.fields import CharField
from rest_framework.utils import field_mapping

from .models import Answer, Choice, Question, Survey

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = (
            "id",
            "title",
            "start_date",
            "end_date",
            "description"
        )

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = [ "id", "choice_text", "is_answer"]

class QuestionSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = [ "id", "question_text", "answer_type", "choice"]
    
class AnswerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Answer
        fields = ('__all__')

class ResultSerializer(serializers.ModelSerializer):
    survey_title = serializers.CharField(source='survey_id.title')
    question_text = serializers.CharField(source='question_id.question_text')
    
    class Meta:
        model = Answer
        fields = ["user_id", "survey_title", "question_text", "answer", "correct"]