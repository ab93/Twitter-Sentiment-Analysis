import sys
import json

def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True


def lines(fp):
    size = str(len(fp.readlines()))
    #print size
    return size


def findHashTags(stream_size):
	responses = []
	responseSize = 0
	hashtag_count = {}

	tweet_file = open(sys.argv[1])
	
	for line in tweet_file:
		response = json.loads(line)
		if "entities" in response:
			if "hashtags" in response["entities"]:
				hashtags = response["entities"]["hashtags"]
				if is_empty(hashtags)==False:
					#print hashtags,'\n'
					responses.append(hashtags)
					responseSize = responseSize + 1

	for i in xrange(responseSize):
		for j in range(len(responses[i])):
			text = responses[i][j]["text"].strip()
			if text in hashtag_count:
				hashtag_count[text] = hashtag_count[text] + 1
			else:
				hashtag_count[text] = 1

	#for key in hashtag_count.keys():
	#	print key,hashtag_count[key]

	sorted_list = sorted(hashtag_count, key=hashtag_count.get, reverse=True)
	#sorted(d.items(), key=lambda x: x[1])
	for index in range(10):
		print '%s %d' % (sorted_list[index],hashtag_count[sorted_list[index]])
		#print sorted_list[index],hashtag_count[sorted_list[index]]
		


def main():
	tweet_file = open(sys.argv[1])
	stream_size = lines(tweet_file)
	findHashTags(stream_size)

	#calculateSentiments(scores,sent_size,tweets,tweet_size)
	


if __name__ == '__main__':
	main()