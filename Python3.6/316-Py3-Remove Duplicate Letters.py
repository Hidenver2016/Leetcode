# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:55:21 2019

@author: hjiang
"""

"""
Given a string which contains only lowercase letters, 
remove duplicate letters so that every letter appear once and only once. 
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
这个题是需要按照原来的str的顺序，不是随意的最小字母排序.
https://blog.csdn.net/fuxuemingzhu/article/details/86063211

这个题的难点在于使得结果是字符串顺序最小。解题思路也是围绕这个展开。

先顺一下思路，首先，每个字符都必须要出现一次，那么当这个字符只有一次机会的时候，必须添加到结果字符串结尾中去，
反之，如果这个字符的次数没有降为0，即后面还有机会，那么可以先把优先级高的放进来，把这个字符放到后面再处理。
所以，我们可以使用一个栈，有点类似单调递增栈的意思，但其实并不是单调栈。我们的思路就是把还可以放到后面的字符弹出栈，
留着以后处理，字符序小的插入到对应的位置。

首先，为了知道每个字符出现了多少次，必须做一次次数统计，这个步骤大家都是知道的。

然后，需要借助一个栈来实现字符串构造的操作。具体操作如下：

从输入字符串中逐个读取字符c，并把c的字符统计减一。

如果当前字符c已经在栈里面出现，那么跳过。

http://www.cnblogs.com/grandyang/p/5085379.html
对于遍历到的字符，先在哈希表中将其值减一，然后看visited中是否被访问过，若访问过则继续循环，
说明该字母已经出现在结果中并且位置已经安排妥当。如果没访问过，我们和结果中最后一个字母比较，
如果该字母的ASCII码小并且结果中的最后一个字母在哈希表中的值不为0(说明后面还会出现这个字母)，
那么我们此时就要在结果中删去最后一个字母且将其标记为未访问，然后加上当前遍历到的字母，
并且将其标记为已访问，以此类推直至遍历完整个字符串s，此时结果里的字符串即为所求。
python代码如下：


栈（stack）又名堆栈，它是一种运算受限的线性表。其限制是仅允许在表的一端进行插入和删除运算。这一端被称为栈顶，相对地，把另一端称为栈底。

"""
import collections
class Solution0(object):#就看这个可以，虽然比较多一点代码，但是容易看懂
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = collections.Counter(s)#首先，为了知道每个字符出现了多少次，必须做一次次数统计
        res = []#最后的答案
        visited = collections.defaultdict(bool)#然后，需要借助一个栈来实现字符串构造的操作
        for c in s:
            count[c] -= 1#从输入字符串中逐个读取字符c，并把c的字符统计减一。
            if visited[c]:#看visited中是否被访问过，若访问过则继续循环，说明该字母已经出现在结果中并且位置已经安排妥当。
                continue
#如果没访问过，我们和结果中最后一个字母比较，如果该字母的ASCII码小并且结果中的最后一个字母在哈希表中的值不为0(说明后面还会出现这个字母)，
#那么我们此时就要在结果中删去最后一个字母且将其标记为未访问，然后加上当前遍历到的字母，
            while res and count[res[-1]] and res[-1] > c:#这个大于号表示ASCII码对比 'b'> 'a' (ASCII码中大写字母在前)
                visited[res[-1]] = False
                res.pop()
            visited[c] = True
            res.append(c)
        return "".join(res)


# Time:  O(n)
# Space: O(k), k is size of the alphabet

#import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        remaining = collections.defaultdict(int)
        for c in s:
            remaining[c] += 1

        in_stack, stk = set(), []
        for c in s:
            if c not in in_stack:
                while stk and stk[-1] > c and remaining[stk[-1]]:
                    in_stack.remove(stk.pop())
                stk += c
                in_stack.add(c)
            remaining[c] -= 1
        return "".join(stk)