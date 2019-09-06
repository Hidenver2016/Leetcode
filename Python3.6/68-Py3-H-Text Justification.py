# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 14:24:20 2019

@author: hjiang
"""
"""
Given an array of words and a width maxWidth, format the text such that each line 
has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
要求尽量均匀的分布空格，如果不行的话，左边空格多于右边
https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
What does this line do? Once you determine that there are only k words that can fit on a given line, 
you know what the total length of those words is num_of_letters. Then the rest are spaces, and there are 
(maxWidth - num_of_letters) of spaces. The "or 1" part is for dealing with the edge case len(cur) == 1.

len(cur)是当前单词数，也是基本空格数；num_of_letters是历史字母数
思路：先往cur里面放单词，当加上新来的单词w，的总长度超过maxWidth时，从右边开始放空格
"""
class Solution:
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:#num_of_letters + len(cur)是已有的单词中字母的长度（num_of_letters）加上单词之间的空格长度len(cur)，包括了最后一个词之后的空格
            if num_of_letters + len(cur) + len(w)  > maxWidth: #len(w)是新单词的长度
                for i in range(maxWidth - num_of_letters):#剩余的都是空格，保证不超过maxWidth
                    cur[i%(len(cur)-1 or 1)] += ' '#在单词之间加空格，先来的先加，保证了右边多左边少。注意len(cur)-1,不把空格放在最后一个词后面，or 1是1个词的边界条件
                res.append(''.join(cur))#用append比较好，如果是用+=和extend就把后面的一段句子全部拆成了字母和空格 res = ['S', 'c', 'i', 'e', 'n', 'c', 'e', ' ', ' ', 'i', 's', ' ', ' ', 'w', 'h', 'a', 't', ' ', 'w', 'e']
                cur, num_of_letters = [], 0
            cur += [w]#这里len(cur)是指有多少个单词，实际上是计算有多少个空格
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

if __name__ == "__main__":
    words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20
    print(Solution().fullJustify(words, maxWidth))













