# -*- coding: utf-8 -*-
"""
Created on Mon May 13 14:28:35 2019

@author: hjiang
"""

"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed.

 

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.


这个题目比较绕
首先建立一个dummy指针，dummy.next指向linklist head
然后换成2->1->3->4, 注意顺序，此时当前指针在1位置
最后才是2->1->4->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a ListNode
    # @return a ListNode    
    def swapPairs(self, head):#比较容易理解
        pre, pre.next = self, head
        while pre.next and pre.next.next:#一定要查看是不是一次有一对，要不是就不用换了
            a = pre.next#第一个
            b = a.next#第二个
            pre.next, b.next, a.next = b, a, b.next#把b（第二个换到第一个）， a在b后面，然后第三个数连着a
            pre = a#直接把当前指针移动到第二个，后面的以此类推
        return self.next
    
    
    # Iteratively
    def swapPairs1(self, head):#                                                     迭代看这个
        dummy = p = ListNode(0)#dummy和p这时候都是在开头，接着p操作交换，最后还是返回dummy.next，指向列表头
        dummy.next = head
        while head and head.next:#注意这个地方p的后面是head，
            tmp = head.next#保存2
            head.next = tmp.next#连接1->3
            tmp.next = head#连接2—>1
            p.next = tmp#把2放在开头
            head = head.next#把head移动到第三个位置
            p = tmp.next#把p也移动到第二个位置
        return dummy.next
     
    # Recursively    
    def swapPairs2(self, head):#                                                         递归看这个，和迭代的套路一样
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs(tmp.next)#建立第一个和第三个之间的联系
            tmp.next = head
            return tmp
        return head
    
class Solution1:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):#                                                            
        if head == None or head.next == None:
            return head
        dummy = ListNode(0); dummy.next = head
        p = dummy
        while p.next and p.next.next:
            tmp = p.next.next#先复制第二个位置 tmp.val=2
            p.next.next = tmp.next#连接1(p.next)的next到3（tmp.next）
            tmp.next = p.next#2的后面（tmp.next）指向1(p.next)
            p.next = tmp#把2移动到head的位置
            p = p.next.next#p直接到第二个位置
        return dummy.next
    
if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
#    head.next.next.next.next = ListNode(5)
    print (Solution().swapPairs1(head))
    
    