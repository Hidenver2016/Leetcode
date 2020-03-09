# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:53:59 2019

@author: hjiang
"""

"""

Write a program to find the node at which the intersection of two singly linked lists begins.
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.
————————————————


For example, the following two linked lists:


begin to intersect at node c1.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. 
There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
 

Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). 
From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. 
There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
 

Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. 
Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
https://blog.csdn.net/fuxuemingzhu/article/details/77631784

双指针
第一次遍历时，如果两者的非公共元素的个数正好相等，那么一定能找到相同元素；如果非公共元素个数不等，
那么在一次遍历之后，两者的指针的差距就是非公共元素的个数差。这样翻转之后，指针的差距正好弥补了非公共元素的差，
这样，第二次遍历要么一定相遇，要么两者没有公共元素，返回None。

分别遍历两个链表，得到分别对应的长度。然后求长度的差值，把较长的那个链表向后移动这个差值的个数，然后一一比较即可。
"""
# Time:  O(m + n)
# Space: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))
        
        
"""
这道题还有一种特别巧妙的方法，虽然题目中强调了链表中不存在环，但是我们可以用环的思想来做，
我们让两条链表分别从各自的开头开始往后遍历，当其中一条遍历到末尾时，我们跳到另一个条链表的开头继续遍历。
两个指针最终会相等，而且只有两种情况，一种情况是在交点处相遇，另一种情况是在各自的末尾的空节点处相等。
为什么一定会相等呢，因为两个指针走过的路程相同，是两个链表的长度之和，所以一定会相等。
这个思路真的很巧妙，而且更重要的是代码写起来特别的简洁，参见代码如下
"""
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):#这个比较巧妙
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        pA = headA
        pB = headB
        while pA is not pB:
            pA = headB if pA is None else pA.next
            pB = headA if pB is None else pB.next
        return pA

"""
分别遍历两个链表，得到分别对应的长度。然后求长度的差值，把较长的那个链表向后移动这个差值的个数，然后一一比较即可。

"""


class Solution1(object):
    def getIntersectionNode(self, headA, headB):#这个容易理解
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len1, len2 = 0, 0
        moveA, moveB = headA, headB
        while moveA:
            len1 += 1
            moveA = moveA.next
        while moveB:
            len2 += 1
            moveB = moveB.next
        if len1 < len2:
            for _ in range(len2 - len1):
                headB = headB.next
        else:
            for _ in range(len1 - len2):
                headA = headA.next
        while headA and headB and headA != headB:#注意这个headA != headB， 应该是题目给出来的，自己写程序写不对
            headA = headA.next
            headB = headB.next
        return headA
    
if __name__ == "__main__":
    headA = ListNode(4)
    headA.next = ListNode(1)
    headA.next.next = ListNode(8)
    headA.next.next.next = ListNode(4)
    headA.next.next.next.next = ListNode(5)
    headB = ListNode(5)
    headB.next = ListNode(0)
    headB.next.next = ListNode(1)
    headB.next.next.next = ListNode(8)
    headB.next.next.next.next = ListNode(4)
    headB.next.next.next.next.next = ListNode(5)
    print (Solution().getIntersectionNode(headA, headB))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    