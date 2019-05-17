# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:50:42 2019

@author: hjiang
"""
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

因此必须先遍历一遍，统计每个节点出现的次数。

第二次遍历的时候，查找下个节点的值出现的次数如果不是1次，那么就删除下个节点。修改这个节点的下个指针指向下下个节点，
这是指向该节点位置的指针不要动，因为还要判断新的next值。
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import collections
class Solution:
    def deleteDuplicates(self, head):# 原式想法
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next
        counter = collections.Counter(val_list)
        head = root
        while head and head.next:
            if counter[head.next.val] != 1:
                head.next = head.next.next
            else:
                head = head.next
        return root.next
    
    def deleteDuplicates1(self, head):#高级搞法
        dummy = pre = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next
