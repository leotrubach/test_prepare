def parse(f):
	questions = []
	for line in f:
		q = {}
		if line.startswith('?'):
			if q:
				r.append(q.copy())
			q = {'question': line[1:], 'answers':[]}
		elif line.startswith('='):
			q['answers'].append({
				'text': line[1:], 'correct': False})
		elif line.startswith('+'):
			q['answers'].append({
				'text': line[1:], 'correct': True})
	return questions