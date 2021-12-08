from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('actualSurveys/', views.ActualSurvey.as_view()),
    path('actualSurveys/<int:surveyId>', views.QuestionsBySurvey.as_view()),
    path('answers/', views.Answers.as_view()),
    path('answers/user/<int:userId>', views.ResultByUser.as_view()),
]