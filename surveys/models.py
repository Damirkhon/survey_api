from django.db import models


class Survey(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date', editable=True)
    end_date = models.DateTimeField('end date')
    description = models.TextField(blank=True)


class Question(models.Model):
    RADIOBUTTON = 1
    MULTIPLE = 2
    TEXT = 3
    TYPES_CHOICES = [
        (RADIOBUTTON, 'Radiobutton'),
        (MULTIPLE, 'Multiple'),
        (TEXT, 'Text'),
    ]
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    answer_type = models.IntegerField(choices=TYPES_CHOICES, default=RADIOBUTTON)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice')
    choice_text = models.CharField(max_length=200)
    is_answer = models.BooleanField(default=False)


class Answer(models.Model):
    user_id = models.IntegerField()
    survey_id = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    correct = models.BooleanField(blank=True, null=True)

    def save(self,*args, **kwargs):
        if self.answer == Choice.objects.filter(question=self.question_id, is_answer=True)[0].choice_text:
            self.correct = True
        else:
            self.correct = False
        return super(Answer, self).save(*args, **kwargs)