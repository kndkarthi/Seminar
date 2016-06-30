
l=[]                                #current tweet list of words
d={None : None,'label':None}        #current tweet word, label pair  
d_main=[]			    #list of all word,label pairs
main=[]				    #list of all words encountered
stopgen={None:None}                 #to calculate frequency of all words

for i in xrange(10):
	f=open('/home/urjeeta/Downloads/seminar/positive/tweet'+str(i)+'.txt','r')
	string=f.read()
	l=string.replace('!',' ').replace('@',' ').replace('#',' ').replace('$',' ').replace('%',' ').replace('^',' ').replace('&',' ').replace('*',' ').replace('(',' ').replace(')',' ').replace('-',' ').replace('_',' ').replace('=',' ').replace('+',' ').replace('\'',' ').replace('\"',' ').replace(':',' ').replace(';',' ').replace('\\',' ').replace('/',' ').replace('|',' ').replace('[',' ').replace(']',' ').replace('{',' ').replace('}',' ').replace('.',' ').replace('>',' ').replace('?',' ').replace(',',' ').replace('<',' ').replace('`',' ').replace('~',' ').split()
	for j in l:
		for k in main:
			k=k.lower()
		j=j.lower()	
		if j not in main:
			d[j]=1
			stopgen[j]=1
			if seminar2.choice==1:			
				d['label']='positive'
			if seminar2.choice==2:			
				d['label']='negative'
			if seminar2.choice==3:			
				d['label']='sarcastic'
						
			main.append(j)		
		else:
			d[j]+=1
			stopgen[j]+=1

		
	d_main.append(d)


print "List of word,value pairs is:\n"

for i in d_main:
	print i
	print "\n"
print "******************************\n"	

print "List of all words:\n"

print main
print "******************************\n"

print "List of word, total value is:\n" 
print stopgen

