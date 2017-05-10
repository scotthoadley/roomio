from django.contrib import admin
from .models import QuestionInstance, Answers, Matches, TrueMatch

# Register your models here.
#admin.site.register(QuestionInstance)
#admin.site.register(Answer)
#admin.site.register(QuestionInstance)
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('question', 'answer_choices')

@admin.register(QuestionInstance)
class QuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'vetted', 'question_option_1', 'question_option_2')
    list_filter = ('question_text', 'vetted', 'question_option_1', 'question_option_2')
   # list_editable = ('question_id', 'question_text', 'vetted')
    fieldsets = (
        (None, {
            'fields': ('question_text', 'vetted',  'question_option_1', 'question_option_2')
        }),
    )

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('question', 'user', 'answer_ideal', 'answer_option', 'answer_weight')
    list_filter = ('question', 'user', 'answer_ideal', 'answer_option', 'answer_weight')
    #list_editable = ('user', 'question', 'answer_weight')


    fieldsets = (
        (None, {
            'fields': ('question', 'user', 'answer_ideal', 'answer_option')
        }),
    )

@admin.register(Matches)
class MatchesAdmin(admin.ModelAdmin):
    list_display = ('question', 'user_one', 'user_two', 'importance_one', 'importance_two', 'total_one', 'total_two')
    list_filter = ('question', 'user_one', 'user_two', 'importance_one', 'importance_two', 'total_one', 'total_two')

    #list_editable = ('user', 'question', 'answer_weight')


    fieldsets = (
        (None, {
            'fields': ('question', 'user_one', 'user_two', 'importance_one', 'importance_two', 'total_one', 'total_two')
        }),
    )

@admin.register(TrueMatch)
class TrueMatchAdmin(admin.ModelAdmin):
    list_display = ('user_onet', 'user_twot', 'match_percent')
    list_filter = ('user_onet', 'user_twot', 'match_percent')

    #list_editable = ('user', 'question', 'answer_weight')


    fieldsets = (
        (None, {
            'fields': ('user_onet', 'user_twot', 'match_percent')
        }),
    )