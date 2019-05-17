# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:49:42 2019

@author: hjiang
"""

"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

做一个判断，走的快的指针如果节点的值一直等于val就一直走；否则快慢指针一起向后走。
https://blog.csdn.net/fuxuemingzhu/article/details/77340945
"""

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
            cur = cur.next
        return dummy.next
    
"""
感觉递归不好写出来。递归函数返回的是删除了val的链表，所以，head.next就是这个链表，然后判断是否相等，
如果相等应该返回的是下一个节点，这个节点就不要了。
"""
class Solution1(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head: return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

