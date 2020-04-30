# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 00:52:31 2020

@author: hjiang
"""

"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""

class Solution(object):
    def frequencySort(self, str):#实在不好排序可以建立两个字典，用value排序，去找key值，这样也是n的时间
        """
        :type str: str
        :rtype: str
        """
        return "".join([char * times for char, times in collections.Counter(str).most_common()])