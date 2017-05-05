from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from random import shuffle
import uuid
from django.conf import settings
from django.db.models.query import QuerySet
from django.db.models.manager import Manager
from django.dispatch import receiver
from django.db.models.signals import post_save

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

    class Meta:
        unique_together = (('created_by', 'question'))

    def get_random_question(self):
        #print("User_id: {}".format(User.get_username()))
        #object_list = list(AnsweFshrs.obsjects.exclude().values()[:1])
        object_list = list(Answers.objects.filter().values())
        shuffle(object_list)
        return object_list[:1]

    def __str__(self):
        return "User: %s Question: %s" % (self.created_by, self.question)

    def get_absolute_url(self):
        return reverse('my-answers')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()