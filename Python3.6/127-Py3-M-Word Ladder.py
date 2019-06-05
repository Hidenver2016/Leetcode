# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:58:00 2019

@author: hjiang
"""

"""
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
https://blog.csdn.net/fuxuemingzhu/article/details/82903681
http://zxi.mytechroad.com/blog/searching/127-word-ladder/   双向要记一下
"""
import collections
class Solution(object):#直接的BFS,写的比较冗余
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        visited = set([beginWord])
        chrs = [chr(ord('a') + i) for i in range(26)]
        bfs = collections.deque([beginWord])
        res = 1
        while bfs:
            len_bfs = len(bfs)
            for _ in range(len_bfs):
                origin = bfs.popleft()
                for i in range(len(origin)):# 对于一个单词中的每一个字符
                    originlist = list(origin)
                    for c in chrs:
                        originlist[i] = c#对于每一个字符，都用26个字母来替换
                        transword = "".join(originlist)#与之前的list(origin)相对应，写的冗余了，可以直接操作字符的
                        if transword not in visited:
                            if transword == endWord:
                                return res + 1
                            elif transword in wordset:
                                bfs.append(transword)
                                visited.add(transword)
            res += 1
        return 0
    
"""
显然上面的这个做法还是可以变短一点的，想起之前的二叉树的BFS的时候，会在每个节点入队列的时候同时保存了这个节点的深度，
这样就少了一层对bfs当前长度的循环，可以使得代码变短。同时，学会了一个技巧，直接把已经遍历过的位置从wordList中删除，
这样就相当于我上面的那个visited数组。下面这个代码很经典了，可以记住。

"""

class Solution1(object):#这个比较好！就看这个就可以了，下面那个估计会写错
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        bfs = []
        bfs.append((beginWord, 1))
        while bfs:
            word, length = bfs.pop(0)
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i + 1:]
                    if newWord in wordset and newWord != word:#既需要在字典以内，又不能走回头路
                        wordset.remove(newWord)#用过以后的删除
                        bfs.append((newWord, length + 1))
        return 0


#双向BFS，非常重要！！！
class Solution2(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordDict = set(wordList)
        if endWord not in wordDict: return 0
        
#        l = len(beginWord)
        s1 = {beginWord}
        s2 = {endWord}
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        wordDict.remove(endWord)
        step = 0
        while len(s1) > 0 and len(s2) > 0:
            step += 1
            if len(s1) > len(s2): s1, s2 = s2, s1 #相互交替
            s = set()   
            for w in s1:
                l = len(w) #感觉加在这里比（比之前那个l = len(beginWord)）较靠的住一点，其实也没差，反正不能改变单词的长度
                new_words = [
                    w[:i] + t + w[i+1:]  for t in lowercase for i in range(l)]
                for new_word in new_words:
                    if new_word in s2: return step + 1 #这个表示对上了，做完了
                    if new_word not in wordDict: continue
                    wordDict.remove(new_word)                        
                    s.add(new_word)
            s1 = s #此句话非常重要！！！
        
        return 0


if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(Solution2().ladderLength(beginWord, endWord, wordList))
















