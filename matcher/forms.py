from django import forms
from .models import Answers, QuestionInstance, Profile, User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from bootstrap3 import *

class AnswerForm(forms.ModelForm):
    question = QuestionInstance.get_random_question(QuestionInstance)
    #answer_weight = forms.CharField()
    class Meta:
         model = Answers
         fields = ('question', 'answer_option', 'answer_weight', 'answer_ideal')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birthdate')