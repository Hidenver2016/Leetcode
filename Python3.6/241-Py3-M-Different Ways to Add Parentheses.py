# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 23:20:41 2019

@author: hjiang
"""

"""
Given a string of numbers and operators, return all possible results from computing 
all the different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1:

Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
"""
#https://blog.csdn.net/fuxuemingzhu/article/details/79568487
"""
如果仔细想一想，能发现这个题和95. Unique Binary Search Trees II基本一模一样，都是分别求出左右的式子的值，然后再用循环拼接在一起。

方法是，循环遍历式子中的每个位置，如果这个位置是运算符，那么把左右的式子分别计算值，然后用运算符拼到一起。
如果上面这个遍历中没有遇到运算符，那么res数组就是空的，这时input是个数字，所以结果把这个数字放进去，再返回即可。
# Time:  O(n * 4^n / n^(3/2)) ~= n * Catalan numbers = n * (C(2n, n) - C(2n, n - 1)),
#                                due to the size of the results is Catalan numbers,
#                                and every way of evaluation is the length of the string,
#                                so the time complexity is at most n * Catalan numbers.
# Space: O(n * 4^n / n^(3/2)), the cache size of lookup is at most n * Catalan numbers.
"""

class Solution(object):#看这个
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        res = list()
        N = len(input)
        for i in range(N):
            if input[i] == "+" or input[i] == "-" or input[i] == "*":
                lefts = self.diffWaysToCompute(input[:i])#这两行就是dfs,直接把公式分解成为数字的级别，然后下面两个循环就是求解
                rights = self.diffWaysToCompute(input[i+1:])
                for left in lefts:
                    for right in rights:
                        if input[i] == "+":
                            res.append(left + right)
                        elif input[i] == "-":
                            res.append(left - right)
                        elif input[i] == "*":
                            res.append(left * right)
        if not res:#如果res里面有数字，证明是经过运算由上面三个判断句加进去的，这时候直作为中间结果接返回给上层就可以了
            res.append(int(input))#这一句非常重要，在dfs中，这个是最后把公式分解成数字，存在res里面，然后返回给上面的left或者right
        return res


#https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66350/1-11-lines-Python-9-lines-C%2B%2B

class Solution1(object):#比较难理解
    def diffWaysToCompute(self, input):
        return [a+b if c == '+' else a-b if c == '-' else a*b
                for i, c in enumerate(input) if c in '+-*'
                for a in self.diffWaysToCompute(input[:i])
                for b in self.diffWaysToCompute(input[i+1:])] or [int(input)]
        
if __name__ == "__main__":
    print(Solution().diffWaysToCompute("2*3-4*5"))