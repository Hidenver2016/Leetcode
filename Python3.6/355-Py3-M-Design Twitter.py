# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 21:53:07 2019

@author: hjiang
"""

"""
Design a simplified version of Twitter where users can post tweets, 
follow/unfollow another user and is able to see the 10 most recent tweets 
in the user's news feed. Your design should support the following methods:

postTweet(userId, tweetId): Compose a new tweet.
getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. 
Each item in the news feed must be posted by users who the user followed or by the user herself.
 Tweets must be ordered from most recent to least recent.
follow(followerId, followeeId): Follower follows a followee.
unfollow(followerId, followeeId): Follower unfollows a followee.
Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);
"""


import heapq

class Twitter(object):#比较复杂，下面那个比较容易

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.followee = {}#是个字典
        

    def postTweet(self, user, tweet):
        self.time += 1
        self.tweets[user] = self.tweets.get(user, []) + [(-self.time,  tweet)]#用一个“-”, 解决排序问题，新的在前，与之后的heapq配合
        
        

    def getNewsFeed(self, user):
        h, tweets = [], self.tweets
        people = self.followee.get(user, set()) | set([user])#得到自己follow的人以及自己，把这些人搞成一个并集
        for person in people:
            if person in tweets and tweets[person]:
                time, tweet = tweets[person][-1]# 取出最新发布的tweet
                h.append((time, tweet, person, len(tweets[person]) - 1))
        heapq.heapify(h)#按照时间来排序，
        news = []
        for _ in range(10):
            if h:
                time, tweet, person, idx = heapq.heappop(h)
                news.append(tweet)
                if idx:#因为之前只取了最新发布的，可能还有tweet没有取完，继续取
                    new_time, new_tweet = tweets[person][idx-1]
                    heapq.heappush(h, (new_time, new_tweet, person, idx - 1))
        return news
    def follow(self, follower, other):
        self.followee[follower] = self.followee.get(follower, set()) | set([other])
        
        

    def unfollow(self, follower, other):
        if follower in self.followee:
            self.followee[follower].discard(other)
    
if __name__ == "__main__":
    twitter = Twitter() 

    twitter.postTweet(1, 5)


    twitter.getNewsFeed(1)


    twitter.follow(1, 2)


    twitter.postTweet(2, 6)

#// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
#// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    twitter.getNewsFeed(1)

#// User 1 unfollows user 2.
    twitter.unfollow(1, 2)

#// User 1's news feed should return a list with 1 tweet id -> [5],
#// since user 1 is no longer following user 2.
    twitter.getNewsFeed(1)
#        
#        
#







import collections, itertools, heapq
class Twitter(object):

    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))#新闻都合并起来，注意这个merge是从小到大自动的
        return [t for _, t in itertools.islice(tweets, 10)]#切片取前面十个，有个一个default的初始值，是 0

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)
            
            
            
            
            
            
            
            
            
            
            
            
            
            