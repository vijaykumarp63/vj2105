def_sort_by_length(words):
	r=[]
	d=dict()
	for word in words:
		d.setdefault(len(word),[]),append(word)
	for key in sorted (d ,reverse=True)
		if len(d[key])>1:
			shuffle(d[key])
		r.extend(d[key])
	return r
