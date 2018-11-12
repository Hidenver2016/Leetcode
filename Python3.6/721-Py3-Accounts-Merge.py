# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 18:56:20 2018

@author: hjiang
"""
#https://blog.csdn.net/likewind1993/article/details/78473302

# Time:  O(nlogn), n is the number of total emails,
#                  and the max length ofemail is 320, p.s. {64}@{255}
# Space: O(n)

import collections


class UnionFind(object):
    def __init__(self):
        self.set = [] # the index of set (list) is the emails, value is the group

    def get_id(self):
        self.set.append(len(self.set))
        return len(self.set)-1

    def find_set(self, x): # find the represent value (or group name) for each email id
        if self.set[x] != x:
            self.set[x] = self.find_set(self.set[x])  # path compression.
        return self.set[x]

    def union_set(self, x, y): # this func is called in single account analyze, different emails needs to be unioned
        x_root, y_root = map(self.find_set, (x, y))
        if x_root != y_root:
#            self.set[min(x_root, y_root)] = max(x_root, y_root)
            self.set[x_root] = y_root


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        union_find = UnionFind()
        email_to_name = {} # email is key and name is content
        email_to_id = {} # email is key, id is the length
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                if account[i] not in email_to_id:
                    email_to_name[account[i]] = name # get email (key) and name (content)
                    email_to_id[account[i]] = union_find.get_id() # get email (key) and id (length)
                union_find.union_set(email_to_id[account[1]],
                                     email_to_id[account[i]])

        result = collections.defaultdict(list)
        for email in email_to_name.keys():
            result[union_find.find_set(email_to_id[email])].append(email) #这一句也是算查漏补缺，因为有时候第一个可能不行
        for emails in result.values():
            emails.sort()
        return [[email_to_name[emails[0]]] + emails
                for emails in result.values()]
        
        
if __name__ == "__main__":
    accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
                ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
    
    
    print (Solution().accountsMerge(accounts))
    
    
    
    
    
    
    
    
    
    
   