from django.contrib import admin
from .models import Survey, Question, Choice, Answer
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

class ChoiceInline(NestedStackedInline):
    model = Choice
    fk_name = 'question'
    extra = 1

class QuestionAdmin(NestedStackedInline):
    model = Question
    fk_name = 'survey'
    extra = 1
    inlines = [ChoiceInline]

class SurveyAdmin(NestedModelAdmin):
    model = Survey
    list_display = ('title', 'end_date')
    inlines = [QuestionAdmin]
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["start_date"]
        else:
            return []

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)