# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 23:44:27 2020

@author: hjiang
"""

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

https://blog.csdn.net/fuxuemingzhu/article/details/72597942
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:        
    def isPalindrome(self, head):#这两个速度差不多，没区别
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
    #    node = None
    #    while slow:
    #        temp = slow.next
    #        slow.next = node
    #        node = slow
    #        slow = temp
        pre, cur = None, slow
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        # compare the first and second half nodes
        while pre: # while node and head:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next
        return True

class Solution1(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        vals = []
        n = 0
        while head:
            vals.append(head.val)
            head = head.next
            n += 1
#        N = len(vals)
        left, right = 0, n-1
        while left < right:
            if vals[left] != vals[right]:
                return False
            left += 1
            right -= 1
        return True
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
#    head.next.next.next.next = ListNode(5)
    print (Solution().isPalindrome(head))
