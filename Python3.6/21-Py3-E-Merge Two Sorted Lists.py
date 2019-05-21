# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:55:29 2019

@author: hjiang
"""

"""
Merge two sorted linked lists and return it as a new list. 
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

直接自己定义一个链表的头，循环两个链表，每次把两个链表头部较小的那个节点放到结尾。最后不要忘了如果链表有剩余，应该拼接起来。
https://blog.csdn.net/fuxuemingzhu/article/details/51291406#Python_34
"""
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        move = head
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2#连接剩下的！
        return head.next