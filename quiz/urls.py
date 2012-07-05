from django.conf.urls import patterns, include, url
from .views import QuizList, QuizDetail, AnswerSubmit

urlpatterns = patterns('',
	url(r'^$', QuizList.as_view(), name='quiz-list'),
	url(r'^(?P<pk>\d+)$', QuizDetail.as_view(), name='quiz-questions'),
	url(r'^submit/$', 
		AnswerSubmit.as_view(), name='submit-answer'),
)