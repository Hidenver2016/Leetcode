# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:51:49 2018

@author: hjiang
"""
"""
You are playing the following Bulls and Cows game with your friend: 
You write down a number and ask your friend to guess what the number is. 
Each time your friend makes a guess, you provide a hint that indicates 
how many digits in said guess match your secret number exactly in both digit and position (called "bulls") 
and how many digits match the secret number but locate in the wrong position (called "cows"). 
Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, 
use A to indicate the bulls and B to indicate the cows. 

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, 
and their lengths are always equal.
"""
#import operator
class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
#        bulls = sum(map(operator.eq, secret, guess))
        bulls = sum(i == j for i, j in zip(secret, guess)) #位置和数字都对的
        both = sum(min(secret.count(x), guess.count(x)) for x in set(guess))# 一共出现了的数字（需要在secret中出现），包括位置对了的，和不对的
        return '%dA%dB' % (bulls, both - bulls)
    
if __name__ == "__main__":
    print(Solution().getHint("1807", "7810"))
    print(Solution().getHint("1123", "0111"))
    
    
    
