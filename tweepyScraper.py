
# coding: utf-8

# In[ ]:


#using tweepy
#https://towardsdatascience.com/how-to-scrape-tweets-from-twitter-59287e20f0f1

#first you must apply on twitters website to become a developer, once you are approved you will be able to use tweepy

#api key = evaOC4OGsWK2YHH5b6mq5DTrb
#api Secret keu = F7dx3ArkgNwvfeFdH9whWbTwJOY682i8FCTZ0Nk59ohRgWMqUe
#bearer token = AAAAAAAAAAAAAAAAAAAAAIi2MAEAAAAAUVcHkc4FBB61bRque%2FS67n%2FrKUs%3D8DTHC9DteLYw6m02qr6mqZ033QIx33Lgo8X1TWOzYl6a0nQ5qY


pip install tweepy

#scraping per user
#example code 
def search_by_user(username)
count = 150
try:     
 # Creation of query method using parameters
 tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
 
 # Pulling information from tweets iterable object
 tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
 
 # Creation of dataframe from tweets list
 # Add or remove columns as you remove tweet information
 tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)

 #scraping for tweets based on text
 #150 most recent tweets regarding the us election
def sesarch_by_text(text_query)
count = 150
try:
 # Creation of query method using parameters
 tweets = tweepy.Cursor(api.search,q=text_query).items(count)
 
 # Pulling information from tweets iterable object
 tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]
 
 # Creation of dataframe from tweets list
 # Add or remove columns as you remove tweet information
 tweets_df = pd.DataFrame(tweets_list)
 
except BaseException as e:
    print('failed on_status,',str(e))
    time.sleep(3)

#searching by hashtags 
def search_for_hashtag(consumer_key, consumer_secret, access_token)
#create authentification for accessing twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
#initialize tweepy API
	api = tweepy.API(auth)
#get the name of the spreadsheet we will write to 
fname = '_'.join(re.findall(r"#(\w+)", userHashtageSearch))

#open the spredsheet we will write to
with open ('%s.csv' % (fname), '') as file: 

	w=csv.writer(file)

	#write header row of spreadsheet 
	w.writerow('timestamp', 'tweet_text' , 'username' , 'all_hashtags' , "followers_count" , "likes" ," retweets")

	#for each tweet matching our hashtags, write relevant info to the spreadsheet
   #getting entry fron user desired hasthtag to search today

  
        for tweet in tweepy.Cursor(api.search, q=userHashtageSearch+' -filter:retweets',                                    lang= , tweet_mode='extended').items(100):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n',' ').encode('utf-8'), tweet.user.screen_name.encode('utf-8'), [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count], tweet.favorite_count, tweet.retweets_count)

#to enter your access codes, the program will prompt you to enter your twitter generated access codes and the hashtags you want to seach for
consumer_key = raw_input('Consumer Key ')
consumer_secret = raw_input('Consumer Secret ')
access_token = raw_input('Access Token ')
access_token_secret = raw_input('Access Token Secret ')
    
userHashtageSearch = raw_input('Which hashtage would you like to search:  ')

if __name__ == '__main__':
    search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase)

#text mining 






