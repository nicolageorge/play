import sys

def parse_reviews(hotels, words):
	ret = {}
	ordered_ids = []

	for k, v in hotels.items():
		rez = 0
		for word in words:
			rez += hotels[k].count(word)

		if k in ret:
			ret[k] += rez
		else:
			ret[k] = rez

	for k, v in sorted(ret.items(), key=operator.itemgetter(1), reverse=True):
		ordered_ids.append(v)
		
	return ' '.join([str(x) for x in ordered_ids])



words = raw_input().lower().strip().split(' ')

inputs = int(raw_input().strip())

hotels = {}

for inp in range(inputs):
	hot_id = int(raw_input().strip())
	hot_review = raw_input().lower().strip().split(' ')
	if hot_id in hotels:
		hotels[hot_id] = hotels[hot_id] + hot_review
	else:
		hotels[hot_id] = hot_review

print parse_reviews(hotels, words)