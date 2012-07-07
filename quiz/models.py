from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Quiz(models.Model):
	name = models.CharField(max_length=40, verbose_name=('name'))

	def __unicode__(self):
		return _('QUIZ: %s') % self.name

	class Meta:
		verbose_name = _('quiz')
		verbose_name_plural = _('quizes')


class Question(models.Model):
	text = models.TextField(verbose_name=_('text'))
	quiz = models.ForeignKey(Quiz, verbose_name=_('quiz'))

	def __unicode__(self):
		return _('QUESTION: %s') % self.text	

	class Meta:
		verbose_name = _('question')
		verbose_name_plural = _('questions')


class Answer(models.Model):
	text = models.TextField(verbose_name=_('text'))
	question = models.ForeignKey(Question, verbose_name=_('question'))
	is_correct = models.BooleanField(verbose_name=_('is correct'))

	def __unicode__(self):
		if self.is_correct:
			return _('ANSWER: %s (correct)') % self.text
		else:
			return _('ANSWER: %s (incorrect)') % self.text

	class Meta:
		verbose_name = _('answer')
		verbose_name_plural = _('answers')


class Submission(models.Model):
	submitted = models.DateTimeField(
		auto_now_add=True,
		verbose_name='submission')
	question = models.ForeignKey(Question, verbose_name=_('question'))
	answer = models.ForeignKey(Answer, verbose_name=_('answer given'))

	def __unicode__(self):
		return _('%(submitted)s -%(question)s -%(answer)s') % {
			'submitted': self.submitted,
			'question': self.question.text,
			'answer': self.answer.text
		}

	def clean(self):
		if False:
			raise ValidationError(_('The answer does not belong to question'))

	class Meta:
		verbose_name = _('submission')
		verbose_name_plural = _('submissions')