# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 15:11:10 2018

@author: hjiang
"""

#Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
#
#Example:
#
#Input:
#[
#  1->4->5,
#  1->3->4,
#  2->6
#]
#Output: 1->1->2->3->4->4->5->6

## Time:  O(nlogk)
## Space: O(1)
#
## Merge k sorted linked lists and return it as one sorted list.
## Analyze and describe its complexity.
#
## Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):		
        if self:		
            return "{} -> {}".format(self.val, self.next)
#
#
## Merge two by two solution.
#class Solution(object):
#    def mergeKLists(self, lists):
#        """
#        :type lists: List[ListNode]
#        :rtype: ListNode
#        """
#        def mergeTwoLists(l1, l2):
#            curr = dummy = ListNode(0)
#            while l1 and l2:
#                if l1.val < l2.val:
#                    curr.next = l1
#                    l1 = l1.next
#                else:
#                    curr.next = l2
#                    l2 = l2.next
#                curr = curr.next
#            curr.next = l1 or l2
#            return dummy.next
#
#        if not lists:
#            return None
#        left, right = 0, len(lists) - 1;
#        while right > 0:
#            if left >= right:
#                left = 0
#            else:
#                lists[left] = mergeTwoLists(lists[left], lists[right])
#                left += 1
#                right -= 1
#        return lists[0]
#
#
## Time:  O(nlogk)
## Space: O(logk)
## Divide and Conquer solution.
#class Solution2:
#    # @param a list of ListNode
#    # @return a ListNode
#    def mergeKLists(self, lists):
#        def mergeTwoLists(l1, l2):
#            curr = dummy = ListNode(0)
#            while l1 and l2:
#                if l1.val < l2.val:
#                    curr.next = l1
#                    l1 = l1.next
#                else:
#                    curr.next = l2
#                    l2 = l2.next
#                curr = curr.next
#            curr.next = l1 or l2
#            return dummy.next
#    
#        def mergeKListsHelper(lists, begin, end):
#            if begin > end:
#                return None
#            if begin == end:
#                return lists[begin]
#            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) / 2), \
#                                 mergeKListsHelper(lists, (begin + end) / 2 + 1, end))
#   
#        return mergeKListsHelper(lists, 0, len(lists) - 1)
#
#
# Time:  O(nlogk)
# Space: O(k)
# Heap solution.
import heapq
class Solution3:#看这个，这个用heap的最简单，其实和用priority queue一样
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        
        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))#把head的val，和linkedlist都压入heap,而heap是按照head.val来排列的
                
        while heap:
            smallest = heapq.heappop(heap)[1]#每次弹出最小的val对应的linkedlist
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))#剩下的节点也要都放进去
                
        return dummy.next
    


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(2)
    list2.next = ListNode(4)
    
    print(Solution3().mergeKLists([list1, list2]))
    
    

    
    
    