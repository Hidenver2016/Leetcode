# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 15:40:56 2019

@author: hjiang
"""

"""
Given a string, determine if a permutation of the string could form a palindrome

Example 1:

Input: "code"
Output: false
Example 2:

Input: "aab"
Output: true
Example 3:

Input: "carerac"
Output: true
"""
# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return sum(v % 2 for v in collections.Counter(s).values()) < 2 #只能有一个字母是奇数

# Time:  O(n)
# Space: O(1)    
    
def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1