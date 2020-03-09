# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:30:55 2019

@author: hjiang
"""

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
https://leetcode.com/problems/reverse-linked-list-ii/discuss/30672/Python-one-pass-iterative-solution
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        p = dummy = ListNode(0)
        dummy.next = head
        for _ in range(m - 1):#到m前一位
            p = p.next
        cur = p.next #m 位
        pre = None
        for _ in range(n - m + 1):
            cur.next, pre, cur = pre, cur, cur.next
        p.next.next = cur#这里是让2指向5，p是1，cur是5
        p.next = pre #pre是换过顺序以后的4，让1连接4
        return dummy.next

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):#看这个，比较稳扎稳打和206可以一起看
        if m == n:
            return head

        dummyNode = ListNode(0)
        dummyNode.next = head
        pre = dummyNode

        for i in range(m - 1):
            pre = pre.next
        
        # reverse the [m, n] nodes
        newHead = None
        cur = pre.next#cur是2
        for i in range(n - m + 1):
            tmp = cur.next
            cur.next = newHead
            newHead = cur
            cur = tmp

        pre.next.next = cur#这里是让2指向5，pre是1，cur是5
        pre.next = newHead#newHead是换过顺序以后的4，让1连接4

        return dummyNode.next
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (Solution().reverseBetween(head, 2,4))