from django.contrib import admin
from .models import Quiz, Question, Answer, Submission


class QuizAdmin(admin.ModelAdmin):
    pass

class AnswerInline(admin.TabularInline):
	model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, ]

class SubmissionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Submission, SubmissionAdmin)