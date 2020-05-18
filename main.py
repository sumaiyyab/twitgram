import jsonlines
import re
import random
import tweets2jsonl as tj
import os.path as path
import sys

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

if __name__ == '__main__':
	if len(sys.argv) > 1:
		user = sys.argv[1]
	else:
		user = input("User to retrieve: ")

	if not path.exists(user+'Twts.jsonl'):
		tj.loadTweets(user)

	dict = {}
	corpus = []
	n = 4

	rtEx = re.compile(r'RT @[\w]+')
	userEx = re.compile(r'@[\w]+')
	mediaEx = re.compile(r'https://t\.co/.+')

	with jsonlines.open(user+'Twts.jsonl') as f:
		for line in f:
			if 'extended_tweet' in line:
				txt = line['extended_tweet']['full_text']
			else:
				txt = line['text']
			if not rtEx.match(txt):
				corpus.append(txt.strip())
	
	print('Working with', len(corpus), 'tweets as input')
	for twt in corpus:
		dict = countNGrams(n, twt, dict)
	real = 0
	for i in range(10):
		ch = chain(n, dict)
		newTwt = chainToString(ch)
		if newTwt in corpus:
			real += 1
		else:
			print(newTwt)
	
	print(real, "tweets generated are existing tweets")
