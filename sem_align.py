from vector_dict import vectors
import numpy as np

def score(prev_pair,w1,w2):
	if w1 in vectors and w2 in vectors:
		a,b = prev_pair
		a,b = vectors[w1] + a, vectors[w2] + b
		a = a/np.sqrt(np.sum(a**2))
		b = b/np.sqrt(np.sum(b**2))
		return (np.dot(a,b),a,b)
	else:
		return (0,0,0)


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
	previous = {}
	back_ptr = {}
	for i in xrange(n+1): previous[i,0] = (0,0)
	for j in xrange(m+1): previous[0,j] = (0,0)
	for i in xrange(1,n+1):
		for j in xrange(1,m+1):
			s,new_vec1,new_vec2 = score(previous[i-1,j-1],a[i-1],b[j-1])
			max_score,back_ptr[i,j] = max(( 
				(s,(pi,pj,keep)) \
					for s,pi,pj,keep in [(s            , i-1, j-1, True),
										 (scores[i-1,j], i-1, j  , False),
										 (scores[i,j-1], i  , j-1, False)]
				),
				key=lambda x:x[0])
			scores[i,j]   = max_score
			previous[i,j] = new_vec1,new_vec2
	i,j = n,m
	pairs = []
	while i and j:
		a_word = a[i-1]
		b_word = b[j-1]
		i,j,keep = back_ptr[i,j]
		if keep:
			pairs.append((a_word,b_word))
	pairs.reverse()
	return pairs,scores[n,m]

print "ALIGN!"
print semantic_align("max screen resolution","maximum laptop display size")
