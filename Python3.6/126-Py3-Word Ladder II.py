# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 21:50:11 2019

@author: hjiang
"""

"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
https://zxi.mytechroad.com/blog/searching/leetcode-126-word-ladder-ii/
https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
https://leetcode.com/problems/word-ladder-ii/discuss/40549/FAST-AND-CLEAN-PythonC%2B%2B-Solution-using-Double-BFS-beats-98

"""
#Python simple BFS layer by layer
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]#在这个dict中，新词是key,旧词或者路径（词路径）是value

        while layer:
            newlayer = collections.defaultdict(list)
            for w in layer:
                if w == endWord: 
                    res.extend(k for k in layer[w])# layer[w]的value表示前面一个单词
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]# 新的key:neww把之前的单词全部加起来,就是形成路径

            wordList -= set(newlayer.keys())#把访问过的值减去，不走回头路
            layer = newlayer#进入下一层

        return res

# 上面那个biBFS 太乱了，没法看，以后自己参照127和上面的代码写一个好了
    
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    