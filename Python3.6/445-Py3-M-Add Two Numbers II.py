# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 00:20:10 2019

@author: hjiang
"""

"""
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

此题重点掌握头插法！！！
解法：
第一，按顺序放入stack
第二，按照标准的add two numbers 相加
第三，用头插法插入linked list

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_list = []
        l2_list = []
        while l1:
            l1_list.append(l1.val)
            l1 = l1.next
            
        while l2:
            l2_list.append(l2.val)
            l2 = l2.next
        
        carry, val = 0,0
        prev,head = None,None
        while l1_list or l2_list:
            val += carry
            if l1_list:
                val += l1_list.pop()
            if l2_list:
                val += l2_list.pop()
                
            carry, val = divmod(val,10)
            head = ListNode(val)#头插法
            head.next = prev
            prev = head
            val = 0
            
        if carry != 0:
            head = ListNode(1)
            head.next = prev
        return head

if __name__ == "__main__":
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
#    l1.next.next.next = ListNode(3)
    print(Solution().addTwoNumbers(l1, l2))

    
    
    
    
    
    
    
    
    
    
    
    