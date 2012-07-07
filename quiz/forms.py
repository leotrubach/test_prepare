from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

from .models import Question, Answer


class SubmitForm(forms.Form):
	question = forms.ModelChoiceField(
		Question.objects.all(), 
		label=_('question'))
	answer = forms.ModelChoiceField(
		Answer.objects.all(), 
		label=_('answer given'))

	def clean(self):
		cleaned_data = super(SubmitForm, self).clean()
		q = self.cleaned_data.get('question')
		a = self.cleaned_data.get('answer')
		if a.question.id != q.id:
			raise ValidationError(_('Answer does not belong to question'))
		return cleaned_data

encodings = (
	('utf_8_sig', 'UTF-8 sig'),
	('cp1251', 'cp1251')
)

class LoadQuizForm(forms.Form):
	title = forms.CharField(max_length=50)
	encoding = forms.ChoiceField(choices=encodings)
	quiz = forms.FileField()