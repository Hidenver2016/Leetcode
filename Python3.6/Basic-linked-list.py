# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:06:29 2018

@author: hjiang
"""

#https://blog.csdn.net/qq490691606/article/details/49948263
#https://zhaochj.github.io/2016/05/12/2016-05-12-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84-%E9%93%BE%E8%A1%A8/

"""节点类"""
class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.pre = None
        self.next = None

"""初始化双向链表"""
class bi_linked_list(object):
    def __init__(self):
        """
        设置头尾，操作比较容易
        头－－（next）－－》尾
        尾－－（pre）－－》头
        :return:
        """
        head = Node()
        tail = Node()
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.pre = self.head
        
#        """获取链表长度"""

    def __len__(self):
        length = 0
        node = self.head
#        while node.next != self.tail:
        while node:
            length += 1
            node = node.next
        return length
    
#    """追加节点"""
    
    def append(self, data):
        """
        :param data:
        :return:
        """
        node = Node(data)
        pre = self.tail.pre
        pre.next = node #前向
        node.pre = pre
        self.tail.pre = node # 后向
        node.next = self.tail
        return node
 
#     """获取节点"""
     
    def get(self, index):
        """
        获取第index个值，若index>0正向获取else 反向获取
        :param index:
        :return:
        """
        length = len(self)
        index = index if index >= 0 else length + index
        if index >= length or index < 0: return None
        node = self.head.next
        while index:
            node = node.next
            index -= 1
        return node
    
#"""设置节点, 知道index,给节点赋值"""

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        return node

#"""插入节点"""

    def insert(self, index, data):
        """
        因为加了头尾节点所以获取节点node就一定存在node.next 和 node.pre
        :param index:
        :param data:
        :return:
        """
        length = len(self)
        if abs(index + 1) > length:
            return False
        index = index if index >= 0 else index + 1 + length
    
        next_node = self.get(index)
        if next_node:
            node = Node(data)
            pre_node = next_node.pre
            pre_node.next = node
            node.pre = pre_node
            node.next = next_node
            next_node.pre = node
            return node
        
#"""删除节点，按照index删除"""

    def delete(self, index):
        node = self.get(index)
        if node:
            node.pre.next = node.next
            node.next.pre = node.pre
            return True
    
        return False

#    """反转链表"""
    def __reversed__(self):
        """
        1.node.next --> node.pre
          node.pre --> node.next
        2.head.next --> None
          tail.pre --> None
        3.head-->tail
         tail-->head
        :return:
        """
        pre_head = self.head
        tail = self.tail
    
        def reverse(pre_node, node):
            if node:
                next_node = node.next
                node.next = pre_node
                pre_node.pre = node
                if pre_node is self.head:
                    pre_node.next = None
                if node is self.tail:
                    node.pre = None
                return reverse(node, next_node)
            else:
                self.head = tail
                self.tail = pre_head
    
        return reverse(self.head, self.head.next)
   

#    """清空链表"""
    def clear(self):
        self.head.next = self.tail
        self.tail.pre = self.head    



if __name__ == '__main__':
    test1 = bi_linked_list()
    print(test1.__len__())
    
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
  
    def is_empty(self):
        return self.head is None
  
    def append(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
  
    def iter(self):
        if not self.head:
            return
        cur = self.head
        yield cur.data
        while cur.next:
            cur = cur.next
            yield cur.data
  
    def insert(self, idx, value):
        cur = self.head
        cur_idx = 0
        if cur is None:             # 判断是否是空链表
            raise Exception('The list is an empty list')
        while cur_idx < idx-1:   # 遍历链表
            cur = cur.next
            if cur is None:   # 判断是不是最后一个元素
                raise Exception('list length less than index')
            cur_idx += 1
        node = Node(value)
        node.next = cur.next
        cur.next = node
        if node.next is None:
            self.tail = node
  
    def remove(self, idx):
        cur = self.head
        cur_idx = 0
        if self.head is None:  # 空链表时
            raise Exception('The list is an empty list')
        while cur_idx < idx-1:
            cur = cur.next
            if cur is None:
                raise Exception('list length less than index')
            cur_idx += 1
        if idx == 0:   # 当删除第一个节点时
            self.head = cur.next
            cur = cur.next
            return
        if self.head is self.tail:   # 当只有一个节点的链表时
            self.head = None
            self.tail = None
            return
        cur.next = cur.next.next
        if cur.next is None:  # 当删除的节点是链表最后一个节点时
            self.tail = cur
  
    def size(self):
        current = self.head
        count = 0
        if current is None:
            return 'The list is an empty list'
        while current is not None:
            count += 1
            current = current.next
        return count
  
    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data == item:
                found = True
            else:
                current = current.next
        return found
  
if __name__ == '__main__':
    link_list = LinkedList()
    for i in range(150):
        link_list.append(i)
#    print(link_list.is_empty())
#    link_list.insert(10, 30)
  
#    link_list.remove(0)
  
    for node in link_list.iter():
        print('node is {0}'.format(node))
    print(link_list.size())
#    print(link_list.search(20))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    