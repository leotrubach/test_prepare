from tempfile import NamedTemporaryFile
import codecs


def parse(f):
	tf = NamedTemporaryFile(delete=False)
	for c in f.chunks():
		tf.write(c)
	tf.close()
	t = codecs.open(tf.name, 'r', encoding='utf_8_sig')
	questions = []
	mode = 'question'
	newmode = ''
	q = {}
	for line in t:
		if mode == 'question':
			if line.startswith('?'):
				q = {'text': line[1:], 'answers':[]}
				newmode = 'answers'
			else:
				newmode = 'question'
		elif mode == 'answers':
			if line.startswith('='):
				q['answers'].append({
					'text': line[1:], 'correct': False})
				newmode = 'answers'
			elif line.startswith('+'):
				q['answers'].append({
					'text': line[1:], 'correct': True})
				newmode = 'answers'
			elif line.startswith('?'):
				questions.append(q.copy())
				q = {'text': line[1:], 'answers':[]}
				newmode = 'question'
			else:
				newmode = 'answers'
		mode = newmode
	return questions