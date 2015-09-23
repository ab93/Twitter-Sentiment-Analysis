import sys
import json

#scores = {}
#responses = []

def init_sentiments(sent_file):
	scores = {}
	for line in sent_file:
		term,score = line.split("\t")
		scores[term] = int(score)
	
	return scores


def parse(stream_size):
	responses = []
	tweets = []
	tweets_size = 0

	tweet_file = open(sys.argv[2])
	
	for line in tweet_file:
	#	print line
		response = json.loads(line)
		responses.append(response)
		if "text" in response:
			tweets.append(response["text"])
			tweets_size = tweets_size + 1

	
	return tweets,tweets_size


def calculateSentiments(scores,sent_size,tweets,tweets_size):
	
	sentimentScores = []
	#print tweets_size
	
	for index in range(tweets_size):    #for each tweet
		words = tweets[index].split(" ")
		sentiment = 0
		for word in words:				#for each word in a tweet
			if word in scores:
				sentiment = sentiment + scores[word]
			
		#print sentiment
		sentimentScores.append(sentiment)

	calculateNewSentiments(sentimentScores, tweets, tweets_size)


def calculateNewSentiments(sentimentScores,tweets,tweets_size):
	
	newSentiments = {}

	for index in range(tweets_size):
		words = tweets[index].split(" ")
		#newSentiment = 0
		for word in words:
			word = word.strip()
			if word not in newSentiments:
				newSentiments[word] = int(0)
			if sentimentScores[index] >= 0:
				newSentiments[word] = newSentiments[word] + ( ((sentimentScores[index]))^2 )
			else:
				newSentiments[word] = newSentiments[word] + ( ((sentimentScores[index]))^3 )
				#print '%s %f' %(word, newSentiments[word]) 
	for word in newSentiments.keys():
		print '%s %f' % (word,newSentiments[word])


def lines(fp):
    size = str(len(fp.readlines()))
    #print size
    return size


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    
    scores = {}
    responses = []

    scores = init_sentiments(sent_file)
    sent_size = lines(sent_file)
    stream_size = lines(tweet_file)
    tweets,tweets_size = parse(stream_size)
    
    #print type(scores)
    #print type(responses)

    calculateSentiments(scores,sent_size,tweets,tweets_size)

    #print scores.items()


if __name__ == '__main__':
    main()
