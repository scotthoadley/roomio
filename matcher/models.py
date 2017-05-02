from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

#class Question(models.Model):


   # question_text = models.CharField(max_length=200, help_text="Enter a question that thrills you about a potential roomate!")

   # def __str__(self):
    #    return self.question_text

# class Answer(models.Model):
#     """
#     Model representing the four different answers possible.
#
#     """
#
#
#     def __str__(self):
#         return "Added answers to question"
#
#     def get_absolute_url(self):
#         return reverse('answer-detail', args=[str(self.id)])


class QuestionInstance(models.Model):
    #id = models.IntegerField(primary_key=True)
    #question = models.ForeignKey('Question', on_delete=models.SET_NULL, null=True)
    question_id = models.AutoField(primary_key=True)
    question_text = models.CharField(max_length=200,
                                     help_text="Enter a question that thrills you about a potential roomate!")
    vetted = models.BooleanField(default = False)

    QUESTION_WEIGHT = (
        ('1', 'Not Important At all'),
        ('25', 'Somewhat Important'),
        ('150', 'Very Important'),
        ('250', 'Mandatory'),
    )

    question_answers = models.CharField(max_length = 3, choices=QUESTION_WEIGHT, blank=True, default="1", help_text='Answer Weighting')

    #hook udp userid who answered this questioninstance here

    #set ordering as random = ?
    class Meta:
        ordering = ['?']

    def __str__(self):
        return '%s' % (self.question_text)

# class Author(models.Model):
    '''
    Stub for when user integration gets put in and can connecction user -> question submitted/answered
    '''