from django.core.management.base import BaseCommand, CommandError
from django.db import models
from matcher.models import Answers, Matches, User, TrueMatch
import itertools
import math

import numpy as np

uanswers = []
sat_answers = []
importance = []
users = []
user_points = []
total_points = []

class Person(object):

    def __init__(self):
        answers = []
        sat_answers = []
        importance = []
        user = User

class Command(BaseCommand):


    help = 'Updates matches.'

    def delete_matches(self):
        Matches.objects.all().delete()
        TrueMatch.objects.all().delete()

    def handle(self, *args, **options):
        global uanswers
        global sat_answers
        global importance
        global users
        global user_points
        global total_points
        importance_one = 0
        importance_two = 0
        total_one = 0
        total_two = 0

        try:
            answers = Answers.objects.order_by('question')
        except:
            raise CommandError('Problem accessing database.')

        self.delete_matches()
        current_question = 1
        for answer in answers:
            if answer.question.id is not current_question:

                #print("-Total Users: {}".format(total_users))
                matched_one = False
                matched_two = False
                print("Question: {}".format(answer.question.question_text))
                for x, y in itertools.combinations(users, 2):
                    print(x, y)
                    print("Indexuans: {} IndexSat: {}".format(uanswers[users.index(x)], sat_answers[users.index(y)]))
                    if uanswers[users.index(x)] == sat_answers[users.index(y)]:
                        print("X matched with Y")
                        importance_one = importance[users.index(x)]
                    #     matched_one = True
                    if uanswers[users.index(y)] == sat_answers[users.index(x)]:
                        print("Y matched with X")
                        importance_two = importance[users.index(y)]
                    #     matched_two = True

                    total_one = importance[users.index(x)]
                    total_two = importance[users.index(y)]
                    print("I1: {} I2: {} Total1: {} Tota21: {}".format(importance_one, importance_two, total_one, total_two))
                    #percent = math.sqrt((importance_one/total) + (importance_two/total))
                    m = Matches(question = answer.question, user_one=x, user_two=y, importance_one=importance_one, importance_two=importance_two, total_one=total_one, total_two=total_two)
                    m.save()

                    importance_one = 0
                    importance_two = 0
                    total_one = 0
                    total_two = 0

                    #
                    # print("Total: {} i_one: {} i_two: {} Matched_1: {} Matched_2: {}".format(total, importance_one, importance_two, matched_one, matched_two))
                    # # match_save = {'user_one': x, 'user_two': y, 'importance_one': importance_one,
                    #               'importance_two': importance_two, 'total': total}
                    # obj = Matches.objects.get_or_create(defaults=match_save)
                    # print(obj)
                    #Matches.objects.update
                #if len(uanswers) > 1:
                    # self.calc_match()
                    # user_points[:] = (value for value in user_points if value != 0)
                    # total_points[:] = (value for value in total_points if value != 0)
                    # percent = [k / l for k, l in zip(user_points, total_points)]
                    # self.stdout.write("Percent: {}".format(percent))
                print("--------New Question----------")
                uanswers = []
                sat_answers = []
                importance = []
                users = []
                user_points = []
                total_points = []
                current_question = answer.question.id


            uanswers.append(answer.answer_option)
            sat_answers.append(answer.answer_ideal)
            importance.append(int(answer.answer_weight))
            users.append(answer.user)
            user_points.append(0)
            total_points.append(0)
            #self.stdout.write("User {} Question_id: {} Answer: {} Ideal: {} importance: {}".format(answer.user, answer.question.id, answer.answer_option, answer.answer_ideal, answer.answer_weight))
            self.stdout.write("User {} Question_id: {} uanswers: {} sat_answers: {} importance: {} Users: {}".format(answer.user, answer.question.id, uanswers, sat_answers, importance, users))

        matcher = Matches.objects.order_by('user_one', 'user_two').distinct()
        match_user_one = ""
        match_user_two = ""
        match_percent = 0
        importance_one = 0
        importance_two = 0
        total_one = 1
        total_two = 1
        percent_one = 0
        percent_two = 0
        first_run = True
        last = len(Matches.objects.all())
        count = 0
        print("LENGTH: {}".format(last))
        for match in matcher:
            count += 1
            print("Count: {}".format(count))
            if first_run:
                match_user_one = match.user_one
                match_user_two = match.user_two
                first_run = False
            importance_one += match.importance_one
            importance_two += match.importance_two
            total_one += match.total_one
            total_two += match.total_two
            print("I1: {}, I2: {}, Total1: {} Total2: {}".format(importance_one, importance_two,
                                                     total_one, total_two))
            if match_user_one != match.user_one or match_user_two != match.user_two:
                percent_one = importance_one/total_one
                percent_two = importance_two/total_two
                match_percent = math.sqrt(percent_one*percent_two)*100
                print("----Total Between {} and {}: {}".format(
                    match_user_one, match_user_two, match_percent
                ))

                real_user1 = User.objects.get(username=match_user_one)
                real_user2 = User.objects.get(username=match_user_two)

               # print("REAL USER----", real_user1)
                tm = TrueMatch(user_onet = real_user1, user_twot = real_user2, match_percent = match_percent)
                tm.save()
                print("----NEW USER----")
                if count != last-1:
                    print("C: {} L: {}".format(count, last))
                    importance_one = 0
                    importance_two = 0
                    total_one = 1
                    total_two = 1
                    percent_one = 0
                    percent_two = 0
            print(match.user_one, match.user_two, match.total_one, match.total_two)
                #print(match.user_one, match.user_two, match.total)

            match_user_one = match.user_one
            match_user_two = match.user_two
            print("MU1: {} MU2: {}".format(match.user_one, match.user_two))

        percent_one = importance_one / total_one
        percent_two = importance_two / total_two
        match_percent = math.sqrt(percent_one * percent_two)*100
        print("----Total Between {} and {}: {}".format(
         match_user_one, match_user_two, match_percent
        ))
        # tm = TrueMatch(user_onet=match.user_one, user_twot=match.user_two, match_percent=match_percent)
        # tm.save()

    #             print("--------New Question--------- -")

    #          #answers_filter = Answers.objects.filter(question__id=answer.question.id)
    #         #for answerf in answer=s_filter:
    #

    #
    #         #self.stdout.write("User_points: {} Total_points: {}".format(user_points, total_points))
    #
    #         current_question = answer.question.id
    #
    #        # poll.opened = False
    #         #poll.save
    #
    def calc_match(self):
        global uanswers
        global sat_answers
        global importance
        global users
        global user_points
        global total_points

        points = [k & l for k, l in zip(uanswers, sat_answers)]
        self.stdout.write("Points: {}".format(points))
        for x in range(0, len(points)):
            if points[x] == 1:
                user_points[x] = user_points[x] + importance[x]
                total_points[x] = total_points[x] + importance[x]
            else:
                total_points[x] = total_points[x] + importance[x]

    #     #np.bitwise_and(uanswers, sat_answers, points)
    #     self.stdout.write("{}".format(points))
    #
    #     #for x,y in itertools.combinations(users, 2):
