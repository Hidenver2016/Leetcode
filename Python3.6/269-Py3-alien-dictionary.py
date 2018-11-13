# Time:  O(n)
# Space: O(|V|+|E|) = O(26 + 26^2) = O(1)


"""There is a new alien language which uses the latin alphabet. 
However, the order among letters are unknown to you. 
You receive a list of words from the dictionary, 
where words are sorted lexicographically by the rules of this new language. 
Derive the order of letters in this language.

For example, Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
] 
The correct order is: "wertf".

Note: You may assume all letters are in lowercase. 
If the order is invalid, return an empty string. 
There may be multiple valid order of letters, return any one of them is fine.

拓扑排序：经典题目就是级联选课（先基础后高级），套路就是先做图，然后找入度为0,然后BFS.其实也可以kahn
https://blog.csdn.net/dm_vincent/article/details/7714519


"""

# BFS solution.
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        result, zero_in_degree_queue, in_degree, out_degree = [], collections.deque(), {}, {}
        nodes = set()
        for word in words: # 提取不重复字母
            for c in word:
                nodes.add(c)
        
        for i in range(1, len(words)): # 每次都要比较两个词，所以是range(1,len(words))
            #前一个词比较长，而且与下一个词共长的区域内，字母一样，则不需学习
            if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]:
                    return ""
            self.findEdges(words[i - 1], words[i], in_degree, out_degree)
        
        for node in nodes: # 找开头
            if node not in in_degree: #找一个入度为零的点
                zero_in_degree_queue.append(node) # 从右边加上
        
        while zero_in_degree_queue:
            precedence = zero_in_degree_queue.popleft() # 从左边弹出，就是pop(0), 就是把一个个入度为零的点弹出来连接
            result.append(precedence)
            
            if precedence in out_degree: # 研究当前点下一个点的集合
                for c in out_degree[precedence]: # 找到当前点的下一个点 （就是当前点出度的点）
                    in_degree[c].discard(precedence) # 在下一个点的入度集合中删掉当前点，免得重复计算
                    if not in_degree[c]: # 确保下一个点再也没有其他上一个点了
                        zero_in_degree_queue.append(c)
            
                del out_degree[precedence] # 研究完了需要删掉，免得重复计算
        
        if out_degree: #这个是边界条件，有点没有连接成图
            return ""

        return "".join(result)


    # Construct the graph. 此处是构建图的出入度关系（字母先后关系），根据上下两个词
    def findEdges(self, word1, word2, in_degree, out_degree):
        str_len = min(len(word1), len(word2)) # 只需要比较最小的部分就可以了
        for i in range(str_len):
            if word1[i] != word2[i]: # 此处开始逐个字母的寻找
                if word2[i] not in in_degree: # 由word1中的字母指向word2的对应位置字母，对于word2来说是入度
                    in_degree[word2[i]] = set() # 此处用set就是要消除重复的元素
                if word1[i] not in out_degree: # 由word1中的字母指向word2的对应位置字母，对于word1来说是出度
                    out_degree[word1[i]] = set()
                in_degree[word2[i]].add(word1[i]) # word1[i] -->word2[i]   f:{t}, word2[i]: {word1[i]}
                out_degree[word1[i]].add(word2[i]) # word1[i] -->word2[i]   t:{f}, word1[i]: {word2[i]}
                break # 找到第一个有规律的就跳出循环


# DFS solution.
class Solution2(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Find ancestors of each node by DFS.
        nodes, ancestors = set(), {}
        for i in range(len(words)): # find all the unique letters in the words
            for c in words[i]:
                nodes.add(c)
#                print nodes
        for node in nodes: # build a empty ancestor dict
            ancestors[node] = []
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]: #一个奇怪的规矩，其实类似于字典的排列，就是要找上下不一样的顺序
                    return "" # here means function failed  函数中的return代表立即结束当前函数，返回指定值
                    print ("hahaha")
            self.findEdges(words[i - 1], words[i], ancestors)

        # Output topological order by DFS.
        result = []
        visited = {}
        print ("nodes", nodes)
        for node in nodes:
            if self.topSortDFS(node, node, ancestors, visited, result):
                return ""  # here means function failed 函数中的return代表立即结束函数，返回指定值
        
        return "".join(result)


    # Construct the graph.
    def findEdges(self, word1, word2, ancestors):
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            if word1[i] != word2[i]:
                ancestors[word2[i]].append(word1[i]) # find the ancestors relationship
                break


    # Topological sort, return whether there is a cycle.
    def topSortDFS(self, root, node, ancestors, visited, result):# 此函数是以root开始不停的找它的前面，对应的查找表就是ancestors
        if node not in visited:
            visited[node] = root
            for ancestor in ancestors[node]:
                print ("ancestor, node, and ancestor[node] are", ancestor, node, ancestors[node])
                if self.topSortDFS(root, ancestor, ancestors, visited, result):# 此处注意第二个参数 ancestor明显说明：已经开始往前面找了
                    return True
            result.append(node)
        elif visited[node] == root:
            # Visited from the same root in the DFS path.
            # So it is cyclic.
            return True
        return False

dict1 = ["wrt","wrf","er","ett","rftt"]
if __name__ == "__main__":
    print (Solution().alienOrder(dict1))
    
    
    
    
    
    
    
    
    