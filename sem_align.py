from vector_dict import vectors
import numpy as np

def score(w1,w2):
	if w1 == w2:
		return 1
	elif w1 in vectors and w2 in vectors:
		val = np.dot(vectors[w1],vectors[w2])
		return val
	else:
		return 0

def semantic_align(string1,string2):
	a = string1.split()
	b = string2.split()
	"Calculates the Levenshtein distance between a and b."
	n, m = len(a), len(b)
	if n > m:
		a,b = b,a
		n,m = m,n
#	print a,b
	scores   = np.zeros((n+1,m+1))
	previous = np.zeros((n+1,m+1,3),dtype=np.int8)
	for i in xrange(1,n+1):
		for j in xrange(1,m+1):
			s = score(a[i-1],b[j-1])
			scores[i,j],previous[i,j,:] = \
				max(((s,(pi,pj,keep))\
						for s,pi,pj,keep in [(scores[i-1,j-1] + s, i-1, j-1, 1),
											 (scores[i-1,j],       i-1, j,   0),
											 (scores[i,j-1],       i,   j-1, 0)]),
					key=lambda x: x[0])
			print (a[i-1],b[j-1],scores[i-1,j-1]+s)
	i,j = n,m
	pairs = []
	while i and j:
		a_word = a[i-1]
		b_word = b[j-1]
		i,j,keep = previous[i,j,:] 
		if keep:
			pairs.append((a_word,b_word))
	return pairs

print semantic_align("max screen resolution","maximum laptop display size")
