import re
import random
import sys
import twint

def countNGrams(n, line, dict):
	line = line.split()
	for i in range(n-1):
		line.insert(0, '<s>')
	line.append('<s>')
	for i in range(len(line)-n+1):
		gram = tuple(line[i:i+n])
		if gram in dict:
			dict[gram] += 1
		else:
			dict[gram] = 1
	return dict


def chain(n, dict):
	chain = []
	possGram = []
	possGramFreq = []
	for gram in dict:
		if gram[0:n-1] == tuple(['<s>'] * (n-1)):
			possGram.append(gram)
			possGramFreq.append(dict[gram])
	chain.append(random.choices(possGram, possGramFreq)[0])
	while chain[-1][-1] != '<s>':
		possGram = []
		possGramFreq = []
		for gram in dict:
			if gram[0:n-1] == chain[-1][1:]:
				possGram.append(gram)
				possGramFreq.append(dict[gram])
		chain.append(random.choices(possGram, possGramFreq)[0])
	return chain	

def chainToString(chain):
	str = ''
	for i in range(len(chain) - 1):
		str += chain[i][-1]
		str += ' '
	return str.strip()

def loadTweets (user):
	c = twint.Config()

	c.Username = user
	c.Store_object = True
	c.Hide_output = True

	twint.run.Search(c)
	return twint.output.tweets_list


if __name__ == '__main__':
	if len(sys.argv) > 2:
		user = sys.argv[1]
		n = sys.argv[2]
	else:
		user = input("User to retrieve: ")
		n = input("n: ")
	n = int(n)

	dict = {}
	corpus = loadTweets(user)

	print('Working with', len(corpus), 'tweets as input')
	for i, twt in enumerate(corpus):
		corpus[i] = twt.tweet
		dict = countNGrams(n, corpus[i], dict)
	real = 0
	for i in range(20):
		ch = chain(n, dict)
		newTwt = chainToString(ch)
		if newTwt in corpus:
			real += 1
		else:
			print(newTwt)
	
	print(real, "tweets generated are existing tweets")
