from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import uuid
from django.conf import settings

# Create your models here.

#class Question(models.Model):


   # question_text = models.CharField(max_length=200, help_text="Enter a question that thrills you about a potential roomate!")

   # def __str__(self):
    #    return self.question_text

class QuestionInstance(models.Model):
    #id = models.IntegerField(primary_key=True)
    #question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200,
                                     help_text="Enter a question that thrills you about a potential roomate!")
    vetted = models.BooleanField(default = False)

    question_option_1 = models.CharField(max_length=200, default="Yes")
    question_option_2 = models.CharField(max_length=200, default="No")
    question_option_3 = models.CharField(max_length=200, default="")
    question_option_4 = models.CharField(max_length=200, default="")

    #set ordering as random = ?
    class Meta:
        ordering = ['?']

    def __str__(self):
        return '%s' % (self.question_text)

    def get_absolute_url(self):
        return "matcher/%i/" % self.question_id

class Answers(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.OneToOneField(QuestionInstance, on_delete=models.SET_NULL, null=True, blank=False)
    answer_option = models.IntegerField(default=1)

    ANSWER_WEIGHT = (
        ('1', 'Not Important At all'),
        ('25', 'Somewhat Important'),
        ('150', 'Very Important'),
        ('250', 'Mandatory'),
    )

    answer_weight = models.CharField(max_length=3, choices=ANSWER_WEIGHT, blank=False, default="1",
                                        help_text='Answer Weighting')

    def __str__(self):
        return "User: %s Question: %s" % (self.created_by, self.question)

    def get_absolute_url(self):
        return reverse('my-answers')