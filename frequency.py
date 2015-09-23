__author__ = 'avik'

import sys
import json

def parse(stream):
	responses = []
	tweets = []
	tweets_size = 0

	tweet_file = open(sys.argv[1])

	for line in tweet_file:
	#	print line
		response = json.loads(line)
		responses.append(response)
		if "text" in response:
			tweets.append(response["text"])
			tweets_size = tweets_size + 1

	#print tweets
	return tweets,tweets_size

def calculateFrequency(tweets,tweets_size):
	frequencies = {}
	occurances = {}
	for tweet in tweets:
		words = tweet.split(" ")
		#words = tweet.strip().split(" ")
		for word in words:
			word = word.strip()
			frequencies[word] = float(0)
			if word in occurances:
				occurances[word] = occurances[word] + 1
			else:
				occurances[word] = float(0)

	
	total = sum(occurances.values())
	for word in frequencies.keys():
		frequencies[word] = occurances[word]/total
	for word in frequencies.keys():
		#print word + ' ' + str(frequencies[word])
		print '%s %f' % (word,frequencies[word])

	

def lines(fp):
    size = str(len(fp.readlines()))
    #print size
    return size


def main():
	tweet_file = open(sys.argv[1])
	stream_size = lines(tweet_file)
	tweets,tweets_size = parse(stream_size)
	calculateFrequency(tweets, tweets_size)

if __name__ == '__main__':
	main()