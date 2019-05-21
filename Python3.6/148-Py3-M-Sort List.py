# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:58:38 2019

@author: hjiang
"""

"""
Sort a linked list in O(n log n) time using constant space complexity.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5
"""
class Solution(object):
    def merge(self, h1, h2):
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, tail, h1 = h1, h1, h1.next
            else:
                tail.next, tail, h2 = h2, h2, h2.next
    
        tail.next = h1 or h2
        return dummy.next
    
    def sortList(self, head):
        if not head or not head.next:
            return head
    
        pre, slow, fast = None, head, head
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None
        
        return self.merge(self.sortList(head), self.sortList(slow))

#https://blog.csdn.net/fuxuemingzhu/article/details/79630742
"""
这个题要求用O(nlongn)的时间复杂度和O(1)的空间复杂度。所以可以使用merge排序，但是如果是链表可以修改指针，把两个有序链表进行原地的合并。

Merge排序就是先划分成一前一后等分的两块，然后对两块分别进行排序，然后再合并两个有序序列。

第一步，如何等分地划分，可以使用快慢指针的方式，当快指针到达结尾，那么慢指针到了中间位置，把链表进行截断分成了两个。

第二步，合并有序的序列，对于单链表来说，正好用到了Merge Two Sorted Lists里的把两个链表合并的方法。

事实上，这个答案里面并不是O(1)的空间，因为，第一，添加了新的链表头的个数会随着递归的次数而不断增加，并不是常量个；第二，递归本身就不是常量空间。

"""
class Solution(object):#这个容易记忆一点
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        pre, slow, fast = head, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None#把前面一半截断
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return self.mergeTwoLists(l1, l2)
    
    def mergeTwoLists(self, l1, l2):
        head = ListNode(0)
        move = head
        if not l1: return l2
        if not l2: return l1
        while l1 and l2:
            if l1.val < l2.val:
                move.next = l1
                l1 = l1.next
            else:
                move.next = l2
                l2 = l2.next
            move = move.next
        move.next = l1 if l1 else l2
        return head.next
