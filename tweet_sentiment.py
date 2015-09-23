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
		#print response.keys()
		#print '\n'	
	
	#for i in range(int(tweets_size)):
		#if "text" in responses[i]:
		#	print responses[i]["text"]
		#	count = count + 1
	#	print tweets[i]
	#	print '\n'
	#print count
	
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
			#	print "yes",word
			#else:
			#	print "no",word
		#print '\n'
		#print sentiment,'\n'
		print sentiment
		sentimentScores.append(sentiment)




def hw():
    print 'Hello, world!'


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
    #hw()
    sent_size = lines(sent_file)
    stream_size = lines(tweet_file)
    tweets,tweets_size = parse(stream_size)
    
    #print type(scores)
    #print type(responses)

    calculateSentiments(scores,sent_size,tweets,tweets_size)
    #print scores.items()


if __name__ == '__main__':
    main()
