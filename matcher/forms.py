from django import forms
from .models import Answers, QuestionInstance, Profile, User

class AnswerForm(forms.Form):
    question = QuestionInstance.get_random_question(QuestionInstance)
    #question = QuestionInstance.objects.get(pk=id)

    def add_answer(self):
        pass

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birthdate')