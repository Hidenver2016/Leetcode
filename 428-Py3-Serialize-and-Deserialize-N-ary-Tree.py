# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 15:57:21 2018

@author: hjiang
"""

"""
Serialization is the process of converting a data structure or object into 
a sequence of bits so that it can be stored in a file or memory buffer, 
or transmitted across a network connection link to be reconstructed later 
in the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree. 
An N-ary tree is a rooted tree in which each node has no more than N children. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that an N-ary tree can be serialized to a string 
and this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree
"1,3,3,2,5,0,6,0,2,0,4,0"

as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, 
so please be creative and come up with different approaches yourself.

Serialize with preorder traversal where sentinel "#" 
indicates the final child of a node has been processed, 
so the function returns to its parent call.
Deserialize by creating a deque (could also use an iterator with next() instead of popleft()).
While the next item is not "#", create a child with the item, 
add the child to the list of children and recurse to create its subtree.
Repeat until there are no more children, then ignore the "#".
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/150790/Python-O(n)-recursive-both-functions
"""

# Time:  O(n)
# Space: O(h)

class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


from collections import deque
class Codec:
    def serialize(self, root):	
        serial = []

        def preorder(node):

            if not node:
                return

            serial.append(str(node.val))

            for child in node.children:
#                print(node.val)# 此处用来显示运行在哪一个节点之下
                preorder(child)

            serial.append("#")      # indicates no more children, continue serialization from parent

        preorder(root)
        return " ".join(serial)

    def deserialize(self, data):	
        if not data:
            return None

        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def helper(node):

            if not tokens:
                return

            while tokens[0] != "#": # add child nodes with subtrees
#                print(node.val)# 此处用来显示运行在哪一个节点之下
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()        # discard the "#"

        helper(root)
        return root

if __name__ == "__main__":
    T = Codec()
    a = T.deserialize("1 3 5 # 6 # # 2 # 4 # #")
    print(T.serialize(a))
    
    
