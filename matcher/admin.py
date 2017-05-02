from django.contrib import admin
from .models import QuestionInstance

# Register your models here.
#admin.site.register(QuestionInstance)
#admin.site.register(Answer)
#admin.site.register(QuestionInstance)
# @admin.register(Answer)
# class AnswerAdmin(admin.ModelAdmin):
#     list_display = ('question', 'answer_choices')

@admin.register(QuestionInstance)
class QuestionInstanceAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_text', 'vetted', 'question_answers')
    list_filter = ('question_id', 'question_text', 'vetted')

    fieldsets = (
        (None, {
            'fields': ('question_text', 'vetted')
        }),
    )