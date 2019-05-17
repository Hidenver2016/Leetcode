# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:48:34 2019

@author: hjiang
"""

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
https://blog.csdn.net/fuxuemingzhu/article/details/51290506
"""

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None
        prev, cur = head, head.next
        while cur:
            if cur.val == prev.val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return head
