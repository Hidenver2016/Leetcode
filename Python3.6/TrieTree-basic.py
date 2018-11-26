# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 18:40:45 2018

@author: hjiang

https://blog.csdn.net/dongtingzhizi/article/details/9796749
"""

class LBTrie:
    """
    simple implemention of Trie in Python by authon liubing, which is not 
    perfect but just to illustrate the basis and principle of Trie. 
    """
    def __init__(self):
        self.trie = {}
        self.size = 0
       
    #添加单词 
    def add(self, word):
        p = self.trie
        word = word.strip()
        for c in word:
            if not c in p:
                p[c] = {}
            p = p[c]
        if word != '':
            #在单词末尾处添加键值''作为标记，即只要某个字符的字典中含有''键即为单词结尾
            p[''] = '' 
      
    #查询单词      
    def search(self, word):
        p = self.trie
        word = word.lstrip()
        for c in word:
            if not c in p:
                return False
            p = p[c]
        #判断单词结束标记''
        if '' in p:
            return True
        return False          
    
    #打印Trie树的接口
    def output(self):
        print ('{')
        self.__print_item(self.trie)    
        print ('}')
        
    
    #实现Trie树打印的私有递归函数，indent控制缩进
    def __print_item(self, p, indent=0):     
        if p:
            ind = '' + '\t' * indent
            for key in p.keys():
                label = "'%s' : " % key
                print (ind + label + '{')
                self.__print_item(p[key], indent+1)
            print (ind + ' '*len(label) + '}' ) 
            
    
if __name__ == '__main__':
    trie_obj = LBTrie()
    #添加单词
    trie_obj.add('hello')
    trie_obj.add('help')
    trie_obj.add('world')
    trie_obj.add('abc')
    #打印构建的Trie树
    trie_obj.output()
    #查找单词     
    if trie_obj.search('hello'):
        print ('Yes')
    else:
        print ('No')
    if trie_obj.search('China'):
        print ('Yes')
    else:
        print ('No')
