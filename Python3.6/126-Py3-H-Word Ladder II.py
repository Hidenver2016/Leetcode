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

与127不同的地方在于需要把所有符合要求的路径打印出来

"""
#Python simple BFS layer by layer
import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):

        wordList = set(wordList)
        res = []
        layer = {}#表示从开始单词hit（beginWord）到当前word的路径，key表示的是最后一个单词，value是hit到当前单词的路径
        layer[beginWord] = [[beginWord]]#在这个dict中，新词是key,旧词或者路径（词路径）是value

        while layer:
            newlayer = collections.defaultdict(list)#存储下一步，找到下一个新单词（这里是对于layer中每一个路径的，每一个w）
            for w in layer: # w是layer中的keys
                if w == endWord: 
                    res.extend(k for k in layer[w])# layer[w]的value表示前面一个单词
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i] + c + w[i + 1:]
                            if neww in wordList:
                                newlayer[neww] += [j + [neww] for j in layer[w]]# 新的key:neww把之前的单词全部加起来,就是形成路径
#                                print('w is', w)
#                                print('newlayer is', newlayer)
#                                print('---')
#                                print('layer is', layer)
#                                print('***')
#注意62行 ‘for w in layer:’， 这个删除是在所有路径走完之后的删除，所以不会（有的词删早了）影响一次更新中的多条路径
            wordList -= set(newlayer.keys())#把访问过的值减去，不走回头路, 
#            print('wordList is', wordList)
#            print('$$$$$$$$$$$$$$$$$$$$$$$$$$')
            layer = newlayer#进入下一层

        return res

    
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution().findLadders(beginWord, endWord, wordList))
    
"""
w is hit
newlayer is defaultdict(<class 'list'>, {'hot': [['hit', 'hot']]})
---
layer is {'hit': [['hit']]}
***
wordList is {'cog', 'dog', 'dot', 'lot', 'log'}
$$$$$$$$$$$$$$$$$$$$$$$$$$
w is hot
newlayer is defaultdict(<class 'list'>, {'dot': [['hit', 'hot', 'dot']]})
---
layer is defaultdict(<class 'list'>, {'hot': [['hit', 'hot']]})
***
w is hot
newlayer is defaultdict(<class 'list'>, {'dot': [['hit', 'hot', 'dot']], 'lot': [['hit', 'hot', 'lot']]})
---
layer is defaultdict(<class 'list'>, {'hot': [['hit', 'hot']]})
***
wordList is {'cog', 'dog', 'log'}
$$$$$$$$$$$$$$$$$$$$$$$$$$
w is dot
newlayer is defaultdict(<class 'list'>, {'dog': [['hit', 'hot', 'dot', 'dog']]})
---
layer is defaultdict(<class 'list'>, {'dot': [['hit', 'hot', 'dot']], 'lot': [['hit', 'hot', 'lot']]})
***
w is lot
newlayer is defaultdict(<class 'list'>, {'dog': [['hit', 'hot', 'dot', 'dog']], 'log': [['hit', 'hot', 'lot', 'log']]})
---
layer is defaultdict(<class 'list'>, {'dot': [['hit', 'hot', 'dot']], 'lot': [['hit', 'hot', 'lot']]})
***
wordList is {'cog'}
$$$$$$$$$$$$$$$$$$$$$$$$$$
w is dog
newlayer is defaultdict(<class 'list'>, {'cog': [['hit', 'hot', 'dot', 'dog', 'cog']]})
---
layer is defaultdict(<class 'list'>, {'dog': [['hit', 'hot', 'dot', 'dog']], 'log': [['hit', 'hot', 'lot', 'log']]})
***
w is log
newlayer is defaultdict(<class 'list'>, {'cog': [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]})
---
layer is defaultdict(<class 'list'>, {'dog': [['hit', 'hot', 'dot', 'dog']], 'log': [['hit', 'hot', 'lot', 'log']]})
***
wordList is set()
$$$$$$$$$$$$$$$$$$$$$$$$$$
wordList is set()
$$$$$$$$$$$$$$$$$$$$$$$$$$
[['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
"""
    
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    