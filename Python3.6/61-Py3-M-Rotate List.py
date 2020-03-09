# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:00:07 2019

@author: hjiang
"""

"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

知道了移动几次，本质上就是把链表的后面k个节点移动到开头去。注意是平移，顺序不变的。所以要找到后面的k个节点，
那么需要用到19. Remove Nth Node From End of List类似的方法，用两个距离为k的指针进行平移操作，当前面的到达了末尾，那么后面的正好是倒数第k个。

找到倒数第k个之后，那么把这个节点和之前的节点断开，把后面的这段移到前面去即可
--------------------- 
原文：https://blog.csdn.net/fuxuemingzhu/article/details/80788107 

"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        _len = 0
        root = head
        while head:
            _len += 1
            head = head.next
        k %= _len
        if k == 0: return root
        fast, slow = root, root
        while k - 1:
            fast = fast.next
            k -= 1
        pre = slow
        while fast.next:#当fast到底之后，slow正好是倒数第k个
            
            pre = slow
            slow = slow.next
            fast = fast.next
        pre.next = None
        fast.next = root
        return slow
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (Solution().rotateRight(head, 2).val)

