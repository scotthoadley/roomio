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

class QuestionInstance(models.Model):
    submitted_user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200,
                                     help_text="Enter a question that thrills you about a potential roomate!")
    vetted = models.BooleanField(default = False)

    question_option_1 = models.CharField(max_length=200, default="Yes")
    question_option_2 = models.CharField(max_length=200, default="No")

    def get_vetted_questions(self):
        return QuestionInstance.objects.filter(vetted__exact=True)

    def get_random_question(self):
        return QuestionInstance.objects.all().order_by('?')[:1].get()

    def __str__(self):
        return '%s' % (self.question_text)

    def get_absolute_url(self):
        return "matcher/%i/" % self.question_id

class Matches(models.Model):
    question = models.ForeignKey(QuestionInstance, on_delete=models.SET_NULL, null=True, blank=False, related_name='question')
    user_one = models.ForeignKey(User, null=True, related_name='user_one')
    user_two = models.ForeignKey(User, null=True, related_name='user_two')
    importance_one = models.IntegerField(default=0)
    importance_two = models.IntegerField(default=0)
    total_one = models.IntegerField(default=0)
    total_two = models.IntegerField(default=0)

class TrueMatch(models.Model):
    user_onet = models.ForeignKey(User, null=True, related_name='user_onet')
    user_twot = models.ForeignKey(User, null=True, related_name='user_twot')
    match_percent = models.FloatField(default=0)

class Answers(models.Model):
    question = models.ForeignKey(QuestionInstance, on_delete=models.SET_NULL, null=True, blank=False)
    #just replace  with question_id
    #question = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    ANSWER_CHOICES = (
      (1, 'Yes'),
     (0, 'No'),
    )

    answer_option = models.IntegerField(default=1, choices=ANSWER_CHOICES)
    answer_ideal = models.IntegerField(default=1, choices=ANSWER_CHOICES)

    ANSWER_WEIGHT = (
      ('0', 'Irrelevant'),
     ('1', 'Somewhat Important'),
    ('10', 'Very Important'),
    ('250', 'Mandatory'),
    )

    answer_weight = models.CharField(max_length=3, choices=ANSWER_WEIGHT, blank=False, default="1",
    help_text='Answer Weighting')

   # class Meta:
        #unique_together = (('created_by', 'question'))

    def __str__(self):
        return "Answer: %s User: %s Question: %s Option: %s Ideal: %s Weight: %s" % (self.id, self.user, self.question_id, self.answer_option, self.answer_ideal, self.answer_weight)

    def get_absolute_url(self):
        return reverse('my-answers')

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length = 500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birthdate = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()