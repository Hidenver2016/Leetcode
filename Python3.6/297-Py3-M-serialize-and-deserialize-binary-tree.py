# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:12:29 2018

@author: hjiang
"""

# Time:  O(n)
# Space: O(h)

# Serialization is the process of converting a data structure or
# object into a sequence of bits so that it can be stored in a file
# or memory buffer, or transmitted across a network connection link
# to be reconstructed later in the same or another computer environment.
#
# Design an algorithm to serialize and deserialize a binary tree. 
# There is no restriction on how your serialization/deserialization
# algorithm should work. You just need to ensure that a binary tree can 
# be serialized to a string and this string can be deserialized to the 
# original tree structure.
#
# For example, you may serialize the following tree
#     1
#   / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes
# a binary tree. You do not necessarily need to follow this format, so 
# please be creative and come up with different approaches yourself.
# Note: Do not use class member/global/static variables to store states. 
# Your serialize and deserialize algorithms should be stateless.
#https://blog.csdn.net/fuxuemingzhu/article/details/79571892
"""
和449. Serialize and Deserialize BST多么的像呀！之前我说，只知道前序遍历是没法确定一个树的，我说的不严谨。
M-如果前序遍历的过程中记录下哪些位置是空节点的话，就是可以确定这棵树的。LeetCode的官方树的构建就是这样的。

因此，我们采用和上题同样的方法，只不过需要把空节点记录下来。然后在反序列化时把它再变成空节点即可
"""
import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:#看这个，比较快

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preOrder(root):
            if not root:
                vals.append('#')
            else:
                vals.append(str(root.val))
                preOrder(root.left)
                preOrder(root.right)
        preOrder(root)
        return ' '.join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(val for val in data.split())
        def build():
            if vals:
                val = vals.popleft() #这个地方要注意，popleft 就是顺序一样也可以建立树，一般是要反着来，对于前序就是右左中（前序本身是中左右）
                if val == '#':
                    return None #遇到"#"直接返回，不再往下面建了
                root = TreeNode(int(val))
                root.left = build()
                root.right = build()
                return root #一个枝建立完备，返回root节点
        return build()
    
if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    nums = Codec().serialize(root)
    print(nums)
    root1 = Codec().deserialize(nums)
    print(root1.val)
    print(root1.left.val)
    print(root1.right.val)
    print(root1.right.left.val)
    print(root1.right.right.val)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


#class Codec1:
#
#    def serialize(self, root):
#        """Encodes a tree to a single string.
#        
#        :type root: TreeNode
#        :rtype: str
#        """
#        def serializeHelper(node):
#            if not node:
#                vals.append('#')
#            else:
#                vals.append(str(node.val))
#                serializeHelper(node.left)
#                serializeHelper(node.right)
#        vals = []
#        serializeHelper(root)
#        return ' '.join(vals)
#
#
#    def deserialize(self, data):
#        """Decodes your encoded data to tree.
#        
#        :type data: str
#        :rtype: TreeNode
#        """
#        def deserializeHelper():
#            val = next(vals)
#            if val == '#':
#                return None
#            else:
#                node = TreeNode(int(val))
#                node.left = deserializeHelper()
#                node.right = deserializeHelper()
#                return node
#        def isplit(source, sep):
#            sepsize = len(sep)
#            start = 0
#            while True:
#                idx = source.find(sep, start)
#                if idx == -1:
#                    yield source[start:]
#                    return
#                yield source[start:idx]
#                start = idx + sepsize
#        vals = iter(isplit(data, ' '))
#        return deserializeHelper()
    
    
