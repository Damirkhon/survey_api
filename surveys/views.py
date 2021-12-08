from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime
from rest_framework import serializers, status
import logging

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Answer, Choice, Question, Survey
from .serializers import AnswerSerializer, QuestionSerializer, ResultSerializer, SurveySerializer

def index(request):
    return HttpResponse("Hello surveys")

class ActualSurvey(APIView):
    def get(self, request, format=None):
        my_date = datetime.now()
        surveys = Survey.objects.filter(start_date__lt=my_date, end_date__gt=my_date).order_by('start_date')
        serializer = SurveySerializer(surveys, many=True)
        return Response(serializer.data)

class QuestionsBySurvey(APIView):
    def get(self, request, surveyId, format=None):
        questions = Question.objects.filter(survey__pk=surveyId)

        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class Answers(APIView):
    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data":serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class ResultByUser(APIView):
    def get(self, request, userId, format=None):
        answers = Answer.objects.filter(user_id=userId)
        serializer = ResultSerializer(answers, many=True)
        return Response(serializer.data)