from django.core.management.base import BaseCommand, CommandError
from django.db import models
from matcher.models import Answers, Matches

uanswers = []
sat_answers = []
importance = []

class Person(object):

    def __init__(self):
        answers = []
        sat_answers = []
        importance = []

class Command(BaseCommand):


    help = 'Updates matches.'

    def handle(self, *args, **options):
        global uanswers
        global sat_answers
        global importance

        try:
            answers = Answers.objects.order_by('question')
        except:
            raise CommandError('Problem accessing database.')


        current_question = 1
        for answer in answers:
            if answer.question.id is not current_question:
                print("New Question")
                uanswers = []
                sat_answers = []
                importance = []
             #answers_filter = Answers.objects.filter(question__id=answer.question.id)
            #for answerf in answer=s_filter:

            uanswers.append(answer.answer_option)
            sat_answers.append(answer.answer_ideal)
            importance.append(int(answer.answer_weight))
            self.stdout.write("User {} Question_id: {} uanswers: {} sat_answers: {} importance: {}".format(answer.user, answer.question.id, uanswers, sat_answers, importance))

            current_question = answer.question.id


        self.stdout.write("Test {}".format(answers))
           # poll.opened = False
            #poll.save

    def calc_save_match(self):
        pass