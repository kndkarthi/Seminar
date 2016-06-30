from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from tweepy import Stream
import json
import pprint
ckey='Your Consumer Key Here'
csecret='Your Consumer Secret Code Here'
atoken='Your Access Token Here'
asecret='Your Access Secret Code Here'

print "1.happy, 2.sad, 3.sarcasm"
choice=int(input())


h=[]

class listn(StreamListener):
		
	def __init__(self, api=None):
                self.api = api 
                self.n = 0
                self.m = 10
		       		
		
	def on_data(self, data):		
		temp=json.loads(data)
		#if temp['retweeted']==False:		
		self.output = open('/home/urjeeta/Downloads/seminar/'+label+'/tweet'+str(self.n)+'.txt', 'w')        	
		self.output.write(temp['text'] + "\n")		
		print '@'+temp['user']['screen_name']+':'+temp['text']
		h.append(temp)
		self.n=self.n+1
		if self.n<self.m: return True
		else: return False

auth=OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream=Stream(auth,listn())

if(choice==1):
	label="positive"
	twitterStream.filter(track=["#happy","#joy"], languages=['en'])
elif(choice==2):
	label="negative"	
	twitterStream.filter(track=["#sad","#angry"], languages=['en'])
elif(choice==3):
	label="sarcastic"
	twitterStream.filter(track=["#sarcasm","#satire","#irony","#sarcastic"], languages=['en'])

print len(h)
