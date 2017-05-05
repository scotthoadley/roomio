from django.contrib import admin
from .models import QuestionInstance, Answers

# Register your models here.
#admin.site.register(QuestionInstance)
#admin.site.register(Answer)
#admin.site.register(QuestionInstance)
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('question', 'answer_choices')

@admin.register(QuestionInstance)
class QuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_text', 'vetted', 'question_option_1', 'question_option_2', 'question_option_3', 'question_option_4')
    list_filter = ('question_id', 'question_text', 'vetted')
   # list_editable = ('question_id', 'question_text', 'vetted')
    fieldsets = (
        (None, {
            'fields': ('question_text', 'vetted',  'question_option_1', 'question_option_2', 'question_option_3', 'question_option_4')
        }),
    )

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ('created_by', 'question', 'answer_weight', 'answer_option')
    list_filter = ('created_by', 'question', 'answer_weight', 'answer_option')
    #list_editable = ('user', 'question', 'answer_weight')


    fieldsets = (
        (None, {
            'fields': ('created_by', 'question', 'answer_weight', 'answer_option')
        }),
    )