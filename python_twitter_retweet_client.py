import twitter,json
import time
import schedule

def run_retweets():
    api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')


    twitter_username = "marcosfreccia"

    HashTags = api.GetSearch(term="#sqlserver",result_type="recent",include_entities=True,count=100)
    for hashs in HashTags:
        tweet_id = hashs.id
        if(hashs.user.screen_name != twitter_username):
            try:
                print(api.PostRetweet(tweet_id))
            except:
                pass
schedule.every(10).minutes.do(run_retweets())

while True:
    schedule.run_pending()
    time.sleep(1)
