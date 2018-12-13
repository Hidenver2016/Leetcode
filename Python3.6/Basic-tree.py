# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 14:47:45 2018

@author: hjiang
"""

#coding=utf-8

class Node(object):
    """节点类"""
    def __init__(self, value=-1, lch=None, rch=None):
        self.value = value
        self.lch = lch
        self.rch = rch


class Tree(object):
    """树类"""
    def __init__(self):
        self.root = Node()
        self.myQueue = []

    def add(self, value):
        """为树添加节点,横着添加"""
        node = Node(value)
        if self.root.value == -1:  # 如果树是空的，则对根节点赋值
            self.root = node
            self.myQueue.append(self.root)
        else:
            treeNode = self.myQueue[0]  # 此结点的子树还没有齐。
            if treeNode.lch == None:
                treeNode.lch = node
                self.myQueue.append(treeNode.lch)
            else:
                treeNode.rch = node
                self.myQueue.append(treeNode.rch)
                self.myQueue.pop(0)  # 如果该结点存在右子树，将此结点丢弃。实现一层层往下走


    def pre_recur(self, root):
        """利用递归实现树的先序遍历"""
        if root == None:
            return
        print (root.value)
        self.pre_recur(root.lch)
        self.pre_recur(root.rch)


    def in_recur(self, root):
        """利用递归实现树的中序遍历"""
        if root == None:
            return
        self.in_recur(root.lch)
        print (root.value)
        self.in_recur(root.rch)


    def post_recur(self, root):
        """利用递归实现树的后序遍历"""
        if root == None:
            return
        self.post_recur(root.lch)
        self.post_recur(root.rch)
        print (root.value)


    def pre_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                print (node.value)
                myStack.append(node)
                node = node.lch
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.rch                  #开始查看它的右子树


    def in_stack(self, root):
        """利用堆栈实现树的中序遍历"""
        if root == None:
            return
        myStack = []
        node = root
        while node or myStack:
            while node:                     #从根节点开始，一直找它的左子树
                myStack.append(node)
                node = node.lch
            node = myStack.pop()            #while结束表示当前节点node为空，即前一个节点没有左子树了
            print (node.value)
            node = node.rch                  #开始查看它的右子树


    def post_stack(self, root):
        """利用堆栈实现树的后序遍历"""
        if root == None:
            return
        myStack1 = []
        myStack2 = []
        node = root
        myStack1.append(node)
        while myStack1:                   #这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = myStack1.pop()
            if node.lch:
                myStack1.append(node.lch)
            if node.rch:
                myStack1.append(node.rch)
            myStack2.append(node)
        while myStack2:                         #将myStack2中的元素出栈，即为后序遍历次序
            print (myStack2.pop().value)


    def BFS(self, root):
        """利用队列实现树的层次遍历"""
        if root == None:
            return
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            node = myQueue.pop(0)
            print (node.value)
            if node.lch != None:
                myQueue.append(node.lch)
            if node.rch != None:
                myQueue.append(node.rch)


if __name__ == '__main__':
    """主函数"""
    values = range(10)           #生成十个数据作为树节点
    tree = Tree()          #新建一个树对象
    for value in values:                  
        tree.add(value)           #逐个添加树的节点

    print ('队列实现层次遍历:')
    tree.BFS(tree.root)

    print ('\n\n递归实现先序遍历:')
    tree.pre_recur(tree.root)
    print ('\n递归实现中序遍历:' )
    tree.in_recur(tree.root)
    print ('\n递归实现后序遍历:')
    tree.post_recur(tree.root)

    print ('\n\n堆栈实现先序遍历:')
    tree.pre_stack(tree.root)
    print ('\n堆栈实现中序遍历:')
    tree.in_stack(tree.root)
    print ('\n堆栈实现后序遍历:')
    tree.post_stack(tree.root)
