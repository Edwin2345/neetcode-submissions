class Twitter:
    #need store tweets by user, and allow for them to follow and unfollow people
    #getNewsfeed needs to combine user tweets and follower tweets and get up to 10 most recent
    #Q: can we assume that tweet ids passed in always increase (ie: mroe recent tweets have larger ids?)
    #  --> No, we need to have a global time variable (simple int) to mark tweets
    #Q: do we need to add vlaidaiton that a perosn acanb't follow/unfollow thems self, posttweet and un/fullow called only on valid useIds, 

    #Data structure: map of userId: Profile
    #Profile will be a class with list of own tweets (time, tweetid) and list of followers (user ids)

    #use time varable that counts down as python only has min heap
    class Profile:
        def __init__(self):
            self.tweets = []
            self.following = set()  
    
    def __init__(self):
        self.tweetTimestamp = 0
        self.userProfiles = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        #create profile if user not exist
        if userId not in self.userProfiles:
           self.userProfiles[userId] = self.Profile()
        
        #append timestamped tweet into users tweet
        self.userProfiles[userId].tweets.append( (self.tweetTimestamp, tweetId) )
        self.tweetTimestamp += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        #user not exist -> just return empty newsFeed (silent fail)
        if userId not in self.userProfiles:
           return [] 

        #make a copy of all tweets from user and there following
        releventTweets = list( self.userProfiles[userId].tweets )
        for followeeId in self.userProfiles[userId].following:
            releventTweets.extend( self.userProfiles[followeeId].tweets )

        #take the ten most recent tweets into a min_heap of size 10
        min_heap = []
        for tweet in releventTweets:
            heapq.heappush(min_heap, tweet)
            if len(min_heap) > 10:
               heapq.heappop(min_heap)
        
        #pop from min heap to get 10 most recent tweets in reverse order
        newsFeed = []
        while len(min_heap) > 0:
            _, tweetId = heapq.heappop(min_heap)
            newsFeed.append(tweetId)
            
        newsFeed.reverse()
        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        #create follower and followeeId profiles if not exist
        if followerId not in self.userProfiles:
           self.userProfiles[followerId] = self.Profile()
        if followeeId not in self.userProfiles:
           self.userProfiles[followeeId] = self.Profile()
        
        self.userProfiles[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #if not actually following -> silently return nothing
        if followeeId not in self.userProfiles[followerId].following:
           return 

        self.userProfiles[followerId].following.remove(followeeId)
        
