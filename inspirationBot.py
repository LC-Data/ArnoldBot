### A snippet of some Inspirational Arnold code ###


argfile = str(sys.argv[1])
consumer_key = "abc"
consumer_secret = "123"
access_token = "789"   ### Your personal values here
access_token_secret = "xyz"

botAuth = tweepy.OAuthHandler(consumer_key, consumer_secret)
botAuth.set_access_token(access_token, access_token_secret)
botAuth.secure = True
api = tweepy.API(botAuth)


def tweetTimer():

	filename=open(argfile,'r')
	f=filename.readlines()
	filename.close()


	for line in f:
	    currentTime = datetime.datetime.now()
	    api.update_status(line)
	    print currentTime.strftime("%H:%M") + "~NEW STATUS TWEETED: " + line
	    time.sleep(14400)#Tweet every 4 hours, 6 tweets daily


    
	###api.update_status('Come with me if you want to lift. https://www.youtube.com/watch?v=vH0nP4NzS9M ')   ###tweet syntax



def followBack():
		
	myFriends = api.friends_ids(api.me().id)


	for follower in tweepy.Cursor(api.followers).items(25):
		currentTime = datetime.datetime.now()
		if follower.id != api.me().id:
			if follower.id not in myFriends:
				follower.follow()
				print currentTime.strftime("%H:%M:%S") + "~now following", follower.screen_name
	#### Make this function recursive for continual followbacks, probably make it in sync with each tweet every however many hours.			


	#for follower in tweepy.Cursor(api.followers).items(25):
	#	if api.show_friendship("comewithme2lift", follower) == False:
	#		follower.follow()
	#		print follower.screen_name
	#		time.sleep(120)



	#for status in api.user_timeline('someuser'):   #FOLLOWING RETWEETER, currently retweets the last TWENTY tweets of 'someuser' from your following list
        #    api.retweet(status.id)






if __name__ == '__main__':
	Thread(target = tweetTimer).start()
	Thread(target = followBack).start()





