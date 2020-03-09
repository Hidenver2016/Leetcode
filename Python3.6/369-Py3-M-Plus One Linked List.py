# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:51:53 2019

@author: hjiang
"""

"""
Given a non-negative integer represented as non-empty a singly linked list of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]


https://www.cnblogs.com/grandyang/p/5626389.html
这道题给了我们一个链表，用来模拟一个三位数，表头是高位，现在让我们进行加1运算，这道题的难点在于链表无法通过坐标来访问元素，
只能通过遍历的方式进行，而这题刚好让我们从链尾开始操作，从后往前，遇到进位也要正确的处理，最后还有可能要在开头补上一位。
那么我们反过来想，如果链尾是高位，那么进行加1运算就方便多了，直接就可以边遍历边进行运算处理，那么我们可以做的就是先把链表翻转一下，
然后现在就是链尾是高位了，我们进行加1处理运算结束后，再把链表翻转回来即可，
"""


#class Solution(object):
#    def plusOne(self, head):
#        """
#        :type head: ListNode
#        :rtype: ListNode
#        """
#        def reverseList(head):#尤其注意这个reverse的写法
##            dummy = ListNode(0)
##            curr = head
##            while curr:
##                dummy.next, curr.next, curr = curr, dummy.next, curr.next
##            return dummy.next
#            cur, pre = head, None
#            while cur:
#                cur.next, pre, cur = pre, cur, cur.next
#            return pre
#
#        rev_head = reverseList(head)
#        curr, carry = rev_head, 1
#        while curr and carry:#这里要修改一下
##            curr.val += carry
##            carry = curr.val // 10
##            curr.val %= 10
#            carry, curr.val = (curr.val + carry)//10, (curr.val + carry)%10
#            if carry and curr.next is None:
#                curr.next = ListNode(0)
#            curr = curr.next
#
#        return reverseList(rev_head)
# Time:  O(n)
# Space: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
        
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def reverseList(head):#尤其注意这个reverse的写法
            cur, pre = head, None
            while cur:
                cur.next, pre, cur = pre, cur, cur.next
            return pre

        rev_head = reverseList(head)
        curr, carry = rev_head, 1
        while curr and carry:#这里要修改一下
            carry, curr.val = (curr.val + carry)//10, (curr.val + carry)%10
            if carry and curr.next is None:
                curr.next = ListNode(0)#下次加上进位即可，就是1
            curr = curr.next

        return reverseList(rev_head)
    
if __name__ == "__main__":
    head = ListNode(9)
#    head.next = ListNode(9)
#    head.next.next = ListNode(3)
#    head.next.next.next = ListNode(4)
#    head.next.next.next.next = ListNode(5)

    print (Solution().plusOne(head).next.val)
    
"""
这里需要注意如果 
a = Solution().plusOne(head)
print(a.val)
print(a.next.val) 会报错，因为此时a已经连加等于2，因此没有next

可以按照上面的方法直接看
"""
    
    
    
    
    
    
    
    
    
    
    