import seminar2

print "1.history 2.conversation 3.topic"
i=int(input())

class lsn(seminar2.StreamListener):
	
	def __init__(self, api=None):
                self.api = api 
                self.n = 0
                self.m = 500


	def on_status(self, status):
		if i==2:
			if str(status.in_reply_to_id) == id_to_check:
				#print , save in list and write to folder of conversation context
				print status.text.encode('utf8')+"\n"				
				self.n=self.n+1
				if self.n<self.m: return True
				else: return False
		if i==1:
			print status.text.encode('utf8')+"\n"
			#print, save in list and write to folder of history context
		if i==3:
			print status.text.encode('utf8')+"\n"
			#print, save in list and write to folder of topic context

tStream=seminar2.Stream(seminar2.auth,lsn())

if i==2:
	#conversation
	for i in seminar2.h:
		id_to_check=i['id_str']   #compare with status.in_reply_to_id
		tStream.filter(track=[]) 
elif i==1:
	#history
	for i in seminar2.h:
		tStream.filter(track=[],follow=[str(i['user']['id'])])	#return last l tweets by author
elif i==3:
	#topic
	for i in seminar2.h:
		hashtags=i['entities']['hashtags']  #check for last l tweets with same hashtag set	
		tStream.filter(track=hashtags)
	
