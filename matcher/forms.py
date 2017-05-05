from django import forms
from .models import Answers, QuestionInstance

class AnswerForm(forms.Form):
    id = Answers.get_random_question(Answers)[0]['question_id']
    question = QuestionInstance.objects.get(pk=id)

    def add_answer(self):
        pass