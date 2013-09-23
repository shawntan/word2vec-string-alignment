import numpy as np
import cPickle as pickle
def load_word2vec(filename):
	word2vec = {}
	#load the word2vec features.
	with open(filename, 'r') as fin:
		next(fin) #skip information on first line
		for line in fin:
			items = line.strip().split(' ')
			word = items[0]
			vect = np.array([float(i) for i in items[1:] if len(i) > 1])
#			vect = vect/np.sqrt(np.sum(vect**2))
			word2vec[word] = vect
	return word2vec


try:
	vectors = pickle.load(open('vectors.data'))
except Exception:
	vectors = load_word2vec('vectors.txt')
	pickle.dump(vectors,open('vectors.data','w'))

if __name__ == "__main__":
	vectors = load_word2vec('vectors.txt')
	pickle.dump(vectors,open('vectors.data','w'))


	
