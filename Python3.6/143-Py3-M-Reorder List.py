# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:57:33 2019

@author: hjiang
"""

"""

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

把一个链表的前半部分正序，后半部分逆序，然后一个一个的连接起来。
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Splits in place a list in two halves, the first half is >= in size than the second.
# @return A tuple containing the heads of the two halves

def reorderList(self, head):#这个比较好理解！！！
    if not head:
        return
        
    # find the mid point
    slow = fast = head 
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse the second half in-place
    pre, cur = None, slow
    while cur:
#        pre, node.next, node = node, pre, node.next
        cur.next, pre, cur = pre, cur, cur.next
    
    # Merge in-place; Note : the last node of "first" and "second" are the same
    first, second = head, pre
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    return




        











