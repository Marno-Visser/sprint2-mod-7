from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
 
import logindetails
 
#TWITTER STREAMER
class TwitterStreamer():
    def __init__(self):
        pass

    def stream_tweets(self, fetched_tweets_filename, hash_tag_list):
        listener = StdOutListener(fetched_tweets_filename)
        auth = OAuthHandler(logindetails.CONSUMER_KEY, logindetails.CONSUMER_SECRET)
        auth.set_access_token(logindetails.ACCESS_TOKEN, logindetails.ACCESS_TOKEN_SECRET)
        stream = Stream(auth, listener) 
        stream.filter(track=hash_tag_list)

#TWITTER STREAM LISTENER
class StdOutListener(StreamListener):
    def __init__(self, fetched_tweets_filename):
        self.fetched_tweets_filename = fetched_tweets_filename
    def on_data(self, data):
        try:
            print(data)
            with open(self.fetched_tweets_filename, 'a') as tf:
                tf.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True
    def on_error(self, status):
        print(status)
        
if __name__ == '__main__':
    hash_tag_list = ["SNAFUClimax", "ReZeroSeason2", "SAO", "GirlsFrontline", "SNAFU"]
    fetched_tweets_filename = "tweets.txt"
    twitter_streamer = TwitterStreamer()
    twitter_streamer.stream_tweets(fetched_tweets_filename, hash_tag_list)

    
