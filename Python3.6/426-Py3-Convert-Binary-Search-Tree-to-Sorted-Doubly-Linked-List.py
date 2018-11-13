# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 20:12:19 2018

@author: hjiang
"""

# Time:  O(n)
# Space: O(h)

# orignal provide
#class Node(object):
#    def __init__(self, val, left, right):
#        self.val = val
#        self.left = left
#        self.right = right





class Node(object):
#    def __init__(self, val, left, right):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        left_head, left_tail, right_head, right_tail = root, root, root, root # 先把中间值root按装上
        if root.left:
            left_head = self.treeToDoublyList(root.left) # 左边已经成双向list，右大左小
            left_tail = left_head.left # 绕个圈
        if root.right:
            right_head = self.treeToDoublyList(root.right) # 右边也是双向list,顺序与左边一致，右大左小
            right_tail = right_head.left # 就是向尾走一步
        left_tail.right, right_head.left = root, root # 搞定左右枝之后，最后来搞root,中间点要握手两边
        root.left, root.right = left_tail, right_head # 还是中间点握手两边
        left_head.left, right_tail.right = right_tail, left_head # 头尾相连即可
        return left_head

if __name__ == "__main__":    
    root = Node(4)
    root.left = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(3)
    root.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(7)
    result = Solution().treeToDoublyList(root)
    print (result.val)
    print (result.right.val)
    print (result.right.right.val)
    print (result.right.right.right.val)
    print (result.right.right.right.right.val)
    print (result.val)
    print (result.left.val)
    print (result.left.left.val)
    print (result.left.left.left.val)
    print (result.left.left.left.left.val)
    





"""

left_head --> left_head.right ... --> left_tail  1 -> 2 -> 3
right_head —-> right.tail.left ... -->right_head 5 -> 6 -> 7

1     


"""







    