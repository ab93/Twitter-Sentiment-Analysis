import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}


def is_empty(any_structure):
    if any_structure:
        #print('Structure is not empty.')
        return False
    else:
        #print('Structure is empty.')
        return True

def init_sentiments(sent_file):
	scores = {}
	for line in sent_file:
		term,score = line.split("\t")
		scores[term] = int(score)
	
	return scores

def lines(fp):
    size = str(len(fp.readlines()))
    #print size
    return size


def parse(stream_size):
	responses = []
	tweets = []
	tweet_size = 0

	tweet_file = open(sys.argv[2])
	
	for line in tweet_file:
	#	print line
		response = json.loads(line)
		responses.append(response)
		if "text" in response:
			tweets.append(response)
			tweet_size = tweet_size + 1

	#for i in range(tweet_size):
		#print tweets[i],'\n'

	return tweets,tweet_size


def calculateSentiments(scores,sent_size,tweets,tweets_size):
	sentimentScores = []
	#print type(tweets[0])
	
	for index in range(tweets_size):    #for each tweet
		words = tweets[index]["text"].split(" ")
		sentiment = 0
		for word in words:				#for each word in a tweet
			if word in scores:
				sentiment = sentiment + scores[word]
			
		#print sentiment
		sentimentScores.append(sentiment)
	
	findState(sentimentScores,sent_size,tweets,tweets_size)



def findState(sentimentScores,sent_size,tweets,tweets_size):
	record = {}
	state_scores = {}
	num_tweets = {}

	for index in range(tweets_size):
		record = tweets[index]
		if "place" in record:		
			if is_empty(record["place"]) == False:
				#print record["place"]["full_name"],'\n'
				place = record["place"]["full_name"].strip().split(",")[0]
				for abbr,full_name in states.items():
					if place == full_name:
						if abbr not in state_scores:
							num_tweets[abbr] = 0
							state_scores[abbr] = 0
						state_scores[abbr] = sentimentScores[index]
						num_tweets[abbr] = num_tweets[abbr] + 1
						#print abbr,state_scores[abbr],place,index
						break
		if "user" in record:
			if record["user"]["location"] != "":
				#print record["user"]["location"],index
				place = record["user"]["location"].strip().split(",")[0]
				for abbr,full_name in states.items():
					if place == full_name:
						if abbr not in state_scores:
							num_tweets[abbr] = 0
							state_scores[abbr] = 0
						state_scores[abbr] = state_scores[abbr] + sentimentScores[index]
						num_tweets[abbr] = num_tweets[abbr] + 1
						#print abbr,state_scores[abbr],place,index
						break

	for place,score in state_scores.items():
		state_scores[place] = float(score)/num_tweets[place]

	max_senti = -99
	for place,score in state_scores.items():
		#print place,score
		if score > max_senti:
			max_senti = score
			happiestState = place
	print happiestState




def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])

	scores = {}

	scores = init_sentiments(sent_file)
	sent_size = lines(sent_file)
	stream_size = lines(tweet_file)
	tweets,tweet_size = parse(stream_size)

	calculateSentiments(scores,sent_size,tweets,tweet_size)
	


if __name__ == '__main__':
	main()