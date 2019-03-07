#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "3267830742-DOdBGfnCOwAND11BLKJFAhhJ2bpv6Q3VXWgKfeL"
access_token_secret = "ppwHO0VbNfHxGuV5kvZ4hyOfxo1okpQTnWmoDBgke5v5d"
consumer_key = "wcJLDajVHHpTAzyIN8KSASXcL"
consumer_secret = "FFQ84DI1PHPxVY9T1EJsxRAgvIRwMOsbQmMLj2xdbiweYuNZWC"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['riverside'])