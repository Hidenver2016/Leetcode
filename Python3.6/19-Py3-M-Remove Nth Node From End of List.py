# -*- coding: utf-8 -*-
"""
Created on Wed May 15 22:46:56 2019

@author: hjiang
"""
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?
https://blog.csdn.net/fuxuemingzhu/article/details/80786149
由于有可能删除首节点，所以使用哑结点当做新的头可以解决。

具体到解法，这个题肯定是使用快慢指针啊，两个之间的距离是n，所以当快指针指向结尾的时候，慢指针正好指向了倒数第n个。
因为要删除慢指针的位置，所以需要一个pre指针记录一下前面的那个节点的位置。
"""
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        root = ListNode(0)
        root.next = head
        fast, slow, pre = root, root, root
        while n - 1:#只需要往前面n-1步即可，这样fast到底之后，slow正好是倒数第n个
            fast = fast.next
            n -= 1
        while fast.next:
            fast = fast.next
            pre = slow#注意这一句，正好保存了前一步的slow
            slow = slow.next
        pre.next = slow.next#删除节点本身很简单
        return root.next
