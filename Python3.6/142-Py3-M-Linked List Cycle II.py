# -*- coding: utf-8 -*-
"""
Created on Thu May 16 17:56:25 2019

@author: hjiang
"""

"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) 
in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

Note: Do not modify the linked list.

 

Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.


 

Follow up:
Can you solve it without using extra space?
https://www.cnblogs.com/grandyang/p/4137302.html
https://blog.csdn.net/fuxuemingzhu/article/details/79530638
这个题要看leetcode的图才可以

还是快慢指针，相遇之后，慢指针回到开头，快慢指针同步走，再相遇的点就是要找的点

下面要证明如果相遇之后，慢指针回到原点继续走再相遇的点在O点。


因为快指针每次走2，慢指针每次走1，快指针走的距离是慢指针的两倍。而快指针又比慢指针多走了一圈。
所以head到环的起点+环的起点到他们相遇的点的距离 与 环一圈的距离相等。
现在重新开始，head运行到环起点 和 相遇点到环起点 的距离也是相等的，
相当于他们同时减掉了 环的起点到他们相遇的点的距离。代码如下：
"""

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next#每次走两步
            slow = slow.next
            if fast == slow:#相遇点
                break
        if not fast or not fast.next:
            return None
        slow = head
        while slow != fast:#相遇之后，慢指针回到原点继续走再相遇的点在O点。
            slow = slow.next
            fast = fast.next
        return fast
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    