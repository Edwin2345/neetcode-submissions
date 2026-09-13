class Twitter:
    #need store tweets by user, and allow for them to follow and unfollow people
    #getNewsfeed needs to combine user tweets and follower tweets and get up to 10 most recent
    #Q: can we assume that tweet ids passed in always increase (ie: mroe recent tweets have larger ids?)
    #  --> No, we need to have a global time variable (simple int) to mark tweets
    #Q: do we need to add vlaidaiton that a perosn acanb't follow/unfollow thems self, posttweet and un/fullow called only on valid useIds, 

    #Data structure: map of userId: Profile
    #Profile will be a class with list of own tweets (time, tweetid) and list of followers (user ids)
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

        #get all possible news feed tweet authors -> user + followes
        authors = set(self.userProfiles[userId].following)
        authors.add(userId)

        #add to min heap the newest tweet from every possible author -> store auhor id asll
        # convert timestamp to negative so min_heap pop most recent firsyt
        min_heap = []
        for authorId in authors:
            authorTweets = self.userProfiles[authorId].tweets
            if len(authorTweets) > 0:
                newestIndex = len(authorTweets) - 1
                timeStamp, tweetId = authorTweets[newestIndex]

                heapq.heappush(min_heap, ( -timeStamp, tweetId, authorId, newestIndex))
        
        #keep popping from min heap until at most size 10 newsfeed -> replenish with 2nd newestIndex 
        newsFeed = []
        while len(min_heap) > 0  and len(newsFeed) < 10:
            _, tweetId, authorId, newestIndex = heapq.heappop(min_heap)
            newsFeed.append(tweetId)

            newestIndex -= 1
            if newestIndex >= 0:
               timeStamp, tweetId = self.userProfiles[authorId].tweets[newestIndex]
               heapq.heappush(min_heap, ( -timeStamp, tweetId, authorId, newestIndex))

        return newsFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        #create follower and followeeId profiles if not exist
        if followerId not in self.userProfiles:
           self.userProfiles[followerId] = self.Profile()
        if followeeId not in self.userProfiles:
           self.userProfiles[followeeId] = self.Profile()
        
        self.userProfiles[followerId].following.add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        #if not a valid follower -> siliently return nothing
        if followerId not in self.userProfiles:
           return
        #if not actually following -> silently return nothing
        if followeeId not in self.userProfiles[followerId].following:
           return 

        self.userProfiles[followerId].following.remove(followeeId)
        
