import json

from django.http import HttpResponseNotAllowed, HttpResponse
from django.views.generic import ListView, DetailView, FormView
from django.shortcuts import redirect

from .models import Quiz, Question, Submission, Answer
from .forms import SubmitForm, LoadQuizForm
from .parser import parse

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

class AnswerSubmit(FormView):
	form_class = SubmitForm
	response_class = HttpResponse

	def get(self, request, *args, **kwargs):
		return HttpResponseNotAllowed('Only post allowed')
	
	def form_valid(self, form):
		s = Submission()
		s.question = form.cleaned_data['question']
		s.answer = form.cleaned_data['answer']
		s.save()
		return self.response_class(
			json.dumps({
				'success': True, 
				'correct': s.answer.is_correct,
				'correct_id': s.question.answer_set.get(is_correct=True).id,
				'given_id': s.answer.id 
			}, encoding='utf-8'),
			content_type = 'application/json'
		)

	def form_invalid(self, form):
		return self.response_class(
			json.dumps({'success': False}, encoding='utf-8'),
			content_type = 'application/json'
		)

class UploadQuizView(FormView):
	form_class = LoadQuizForm
	template_name = 'quiz/upload_quiz.html'

	def form_valid(self, form):
		questions = parse(form.cleaned_data.get('quiz'))
		print questions
		quiz = Quiz(name=form.cleaned_data.get('title'))
		quiz.save()
		for q in questions:
			qn = Question(text=q['text'], quiz=quiz)
			qn.save()
			for a in q['answers']:
				ans = Answer(
					text=a['text'], 
					is_correct=a['correct'],
					question=qn)
				ans.save()
		return redirect('quiz-list')

	def form_invalid(self, form):
		return redirect('quiz-list')