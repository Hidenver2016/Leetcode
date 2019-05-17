# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:29:18 2019

@author: hjiang
"""

"""

Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...
我的想法很朴素。我只用弄出来两条链不就好了吗？如果是奇数节点放到奇链，如果是偶数节点就放到偶链。最后，把偶链放到奇链的后面就好了。

注意，偶链的末尾指针要设置成空，已让单链表终止。

比如对于用例[1,2,3]，奇数链是1->3，偶链是2，而遍历完成后的偶链2仍然指向3的，所以死循环了。把尾指针设置成空就能终止了。
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/79569396 

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
# Time:  O(n)
# Space: O(1) 
class Solution(object):
    def oddEvenList(self, head):#看这个把，思想简单
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd = ListNode(0)
        even = ListNode(0)
        oddHead, evenHead = odd, even#odd, even去操作列表，oddHead, evenHead还是操作表头
        index = 0
        while head:
            if index & 1 == 0:#奇数
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            head = head.next
            index += 1
        even.next = None#链表终止
        odd.next = evenHead.next#链表连接
        return oddHead.next
    
    
    
    
    
    
    
    
    
    
    
    
    
