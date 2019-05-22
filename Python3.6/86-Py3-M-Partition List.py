# -*- coding: utf-8 -*-
"""
Created on Thu May 16 18:00:52 2019

@author: hjiang
"""

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5


题目大意
要把一个单链表中，小于某个数字的所有节点放到前面，其余的位置都不要变化。

解题方法
乍一看，感觉原地做这些操作很难。但是，我们换个思路就感觉很简单了。

做链表的题，不要省指针。

用两个新指针，分别记录比x值小的和比x值大的，遍历原来的链表的时候根据值的大小拼接到对应的链表后面。

最后再把两个链表拼接到一起就行了。
--------------------- 

原文：https://blog.csdn.net/fuxuemingzhu/article/details/80793501 

"""
class Solution(object):
    def partition(self, head, x):
        h1 = l1 = ListNode(0)
        h2 = l2 = ListNode(0)
        while head:
            if head.val < x:
                l1.next = head
                l1 = l1.next
            else:
                l2.next = head
                l2 = l2.next
            head = head.next
        l2.next = None
        l1.next = h2.next
        return h1.next