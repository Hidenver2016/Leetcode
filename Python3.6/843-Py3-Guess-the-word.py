# -*- coding: utf-8 -*-
"""
Created on Mon Nov 19 17:54:17 2018

@author: hjiang
"""

"""
This problem is an interactive problem new to the LeetCode platform.

We are given a word list of unique words, each word is 6 letters long, 
and one word in this list is chosen as secret.

You may call master.guess(word) to guess a word.  The guessed word should have type string 
and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) 
of your guess to the secret word.  Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have 10 guesses to guess the word. At the end of any number of calls, 
if you have made 10 or less calls to master.guess and at least one of these guesses was the secret, 
you pass the testcase.

Besides the example test case below, there will be 5 additional test cases, 
each with 100 words in the word list.  The letters of each word in those testcases 
were chosen independently at random from 'a' to 'z', such that every word in the given word lists is unique.

Example 1:
Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]

Explanation:

master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.

We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Note:  Any solutions that attempt to circumvent the judge will result in disqualification.
解题关键：一定要在wordlist中间找出相似长度一样的词来组成新的wordlist继续搜索（一定要一样长）
"""


# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
class Master:
    def guess(self, word):
        """
        :type word: str
        :rtype int
        """
        count = 0
        key_word = "acckzz"
        count = sum(i == j for i, j in zip(key_word, word))
        return count
        
import random
#class Solution:
#    def findSecretWord(self, wordlist, master):
#        n = 0
#        while n < 6:
#            guess = random.choice(wordlist)
#            n = master.guess(guess)
#            wordlist = [w for w in wordlist if sum(i == j for i, j in zip(guess, w)) == n]
            
#import random
#Time: O(n level)
#Space: O(n) 
class Solution1(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        def num_of_same(aa, bb):
            return sum([a == b for a, b in zip(aa,bb)])
        
        random.shuffle(wordlist) # 把wordlist 随机排序
        pool = [word for word in wordlist]
        
        while pool:
            word = pool.pop()
            num_same = master.guess(word)
            if num_same == len(word):
                return word
            pool = [ word2 for word2 in pool if num_of_same(word,word2) == num_same] #关键点，相似长度一样
        return -1
    
if __name__ == "__main__":
    T = Master()
    print(Solution1().findSecretWord(["acckzz","ccbazz","eiowzz","abcczz"], T))
    
    