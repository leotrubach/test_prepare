from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Quiz, Question, Submission


class QuizList(ListView):
	model = Quiz

class QuizDetail(DetailView):
	model = Quiz

	def get_context_data(self, **kwargs):
		context = super(QuizDetail, self).get_context_data(**kwargs)
		random_question = Question.objects.filter(
			quiz=self.object).order_by('?')[0]
		shuffled_answers = random_question.answer_set.order_by('?')
		context['question'] = random_question
		context['answers'] = shuffled_answers
		return context

class AnswerSubmit(CreateView):
	model = Submission
