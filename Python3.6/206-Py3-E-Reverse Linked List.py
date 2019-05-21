# -*- coding: utf-8 -*-
"""
Created on Sun May 12 22:37:46 2019

@author: hjiang
"""
"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


注意369里面reverse linklist的写法，这个写法需要固定下来
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

#迭代
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        newHead = None# newhead实际上是newtail
        while head != None:
            temp = head.next# 先复制第二个位置的节点
            head.next = newHead#第一个位置的节点的下一步指向空，或是上一个节点（第一次循环是1->Null, 第二次循环是2->1）
            newHead = head#新节点平移到head
            head = temp#head去之前的下一个节点
        return newHead
    
    def reverseList1(self, head):#高级迭代
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur, prev = head, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev
#递归   
class Solution1(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverse(head, None)
        
    def reverse(self, head, newHead):
        if not head:
            return newHead
        temp = head.next
        head.next = newHead
        return self.reverse(temp, head)
    
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (Solution().reverseList(head))
