class Twitter:
    # map userId ; profile object
    # profile: following (includes themselve and id's of those they follow), tweets (timestamp, id's)
    # timestamp is jsut a simple int counter we decrement every post to use native min_heap
    # most recent will have larget timestamp
    class Profile:
        def __init__(self):
            self.following = set()
            self.tweets = [] # (timestamp, tweetId)

    def __init__(self):
        self.userMap = {}  # userId to profile
        self.timestamp = 0

    #selfper function to add user to map, and follow themselve ot reciev there twees
    def createUser(self, userId):
        self.userMap[userId] = self.Profile()
        self.userMap[userId].following.add(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # create user if not exist
        if userId not in self.userMap:
            self.createUser(userId)

        # append latest tweet and  decrement timestamp
        user = self.userMap[userId]
        user.tweets.append( (self.timestamp, tweetId) )
        self.timestamp -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        #user DNE
        if userId not in self.userMap:
           return []
        user = self.userMap[userId]

        #add the latest tweet for each follower to min_heap
        min_heap = []
        for followeeId in user.following:
            followee = self.userMap[followeeId]
            if len(followee.tweets) > 0:
               tweetIndex = len(followee.tweets)-1
               timestamp, tweetId = followee.tweets[tweetIndex] 
               heapq.heappush(min_heap, (timestamp, tweetIndex, tweetId, followeeId))
        
        #get up to 10 tweets,
        recentTweets = []
        while len(min_heap) > 0 and len(recentTweets) < 10:
            #take most recent tweet
            _, tweetIndex, tweetId, followeeId = heapq.heappop(min_heap)
            recentTweets.append( tweetId )

            #replenish heap with next most recent for that follower
            tweetIndex -= 1
            if tweetIndex >= 0:
               timestamp, tweetId = self.userMap[followeeId].tweets[tweetIndex]
               heapq.heappush(min_heap, (timestamp, tweetIndex, tweetId, followeeId) ) 
        
        return recentTweets


    def follow(self, followerId: int, followeeId: int) -> None:
        # create user if either not exist
        if followerId not in self.userMap:
            self.createUser(followerId)
        if followeeId not in self.userMap:
            self.createUser(followeeId)
        
        # follower followes folllowee
        follower = self.userMap[ followerId ]
        follower.following.add( followeeId )
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        #error: either one DNE
        if followerId not in self.userMap or followeeId not in self.userMap:
           return
        #follower not acutlly following followee
        if followeeId not in self.userMap[ followerId ].following:
           return 

        # follower removes followee from following llist
        follower = self.userMap[ followerId ]
        follower.following.remove( followeeId ) 
