# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:52:43 2019

@author: hjiang
"""

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
先求和，再构建链表。这个方法比较暴力。
"""

class Solution(object):
    def addTwoNumbers(self, l1, l2):#暴力法不推荐
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ''
        num2 = ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        add = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        head = ListNode(add[0])
        answer = head
        for i in range(1, len(add)):
            node = ListNode(add[i])
            head.next = node
            head = head.next
        return answer
    
"""
这个题目不用倒序，链表第一位就是各位，所以可以直接求
"""
    
class Solution1(object):
    def addTwoNumbers(self, l1, l2):#看这个
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = (v1 + v2 + carry) // 10, (v1 + v2 + carry) % 10
#            val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



