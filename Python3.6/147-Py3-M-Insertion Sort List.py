# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:04:46 2019

@author: hjiang
"""

"""
Sort a linked list using insertion sort.


A graphical example of insertion sort. The partial sorted list (black) initially 
contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted 
in-place into the sorted list
 

Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, 
finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):#没必要这么复杂，直接搞成linkedlist，排序，然后还原成linkedlist即可
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        root = TreeNode(0)
        root.next = head
        while head.next:
            if head.val <= head.next.val:
                head = head.next
            else:
                temp = head.next
                q = root
                head.next = head.next.next#直接后移
                while q.next and q.next.val < temp.val:
                    q = q.next#找到temp合适的位置
                temp.next = q.next
                q.next = temp
        return root.next
