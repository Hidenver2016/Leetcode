# -*- coding: utf-8 -*-
"""
Created on Tue Dec  4 11:34:53 2018

@author: hjiang
"""

"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: 
    TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.  In the case of a tie, 
the most recent vote (among tied candidates) wins.

 

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
 

Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].

Intuition:
Initialization part:

In the order of time, we count the number of votes for each person.
Also, we update the current lead of votes for each time point.
if (count[person] >= count[lead]) lead = person
Time Complexity: O(N)

Query part:
Binary search t in times, find out the latest time point no later than t.
Return the lead of votes at that time point.
Time Complexity: O(logN)

"""
import bisect
class TopVotedCandidate0(object):

    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for t, p in zip(times, persons):
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0): lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]
    


    
if __name__ == "__main__":
    T = TopVotedCandidate0([0,1,1,0,0,1,0],[0,5,10,15,20,25,30])
    print(T.q(25))
    
#class TopVotedCandidate1(object):
#
#    def __init__(self, persons, times):
#        """
#        :type persons: List[int]
#        :type times: List[int]
#        """
#        self.leads, self.times, count = [], times, {}
#        lead = -1
#        for p, t in zip(persons, times):
#            count[p] = count.get(p, 0) + 1
#            if count.get(lead, 0) <= count[p]:
#                lead = p
#            self.leads.append(lead)
#            
#    def q(self, t):
#        """
#        :type t: int
#        :rtype: int
#        """
#        l, r = 0, len(self.times) - 1
#        while l <= r:
#            mid = (l + r) // 2
#            if self.times[mid] == t:
#                return self.leads[mid]
#            elif self.times[mid] > t:
#                r = mid - 1
#            else:
#                l = mid + 1
#        return self.leads[l - 1]
    
    
    
    
    
    
    
    
    
    
    
    
    