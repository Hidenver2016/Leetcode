# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 18:10:29 2019

@author: hjiang
"""

"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, 
find the area of largest rectangle in the histogram.

 


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

 


The largest rectangle is shown in the shaded area, which has area = 10 unit.

 

Example:

Input: [2,1,5,6,2,3]
Output: 10
http://www.cnblogs.com/grandyang/p/4322653.html
http://www.cnblogs.com/grandyang/p/8887985.html

因此我们需要一个递增栈，当遇到大的数字直接进栈，而当遇到小于栈顶元素的数字时，就要取出栈顶元素进行处理了

递增栈是维护递增的顺序，当遇到小于栈顶元素的数就开始处理，而递减栈正好相反，维护递减的顺序，当遇到大于栈顶元素的数开始处理。
那么根据这道题的特点，我们需要按从高板子到低板子的顺序处理，先处理最高的板子，宽度为1，然后再处理旁边矮一些的板子，此时长度为2，
因为之前的高板子可组成矮板子的矩形 ，因此我们需要一个递增栈，当遇到大的数字直接进栈，而当遇到小于栈顶元素的数字时，就要取出栈顶元素进行处理了，
那取出的顺序就是从高板子到矮板子了，于是乎遇到的较小的数字只是一个触发，表示现在需要开始计算矩形面积了，为了使得最后一块板子也被处理，
这里用了个小trick，在高度数组最后面加上一个0，这样原先的最后一个板子也可以被处理了。

由于栈顶元素是矩形的高度，那么关键就是求出来宽度，那么跟之前那道 Trapping Rain Water 一样，单调栈中不能放高度，而是需要放坐标。
由于我们先取出栈中最高的板子，那么就可以先算出长度为1的矩形面积了，然后再取下一个板子，此时根据矮板子的高度算长度为2的矩形面积，
以此类推，知道数字大于栈顶元素为止，再次进栈，巧妙的一比！关于单调栈问题可以参见博主的一篇总结帖 LeetCode Monotonous Stack Summary 单调栈小结，
代码如下：

单调递增栈可以找到左起第一个比当前数字小的元素。比如数组 [2 1 4 6 5]，刚开始2入栈，数字1入栈的时候，发现栈顶元素2比较大，将2移出栈，此时1入栈。
那么2和1都没左起比自身小的数字。然后数字4入栈的时候，栈顶元素1小于4，于是1就是4左起第一个小的数字。此时栈里有1和4，然后数字6入栈的时候，
栈顶元素4小于6，于是4就是6左起第一个小的数字。此时栈里有1，4，6，然后数字5入栈的时候，栈顶元素6大于5，将6移除，此时新的栈顶元素4小于5，
那么4就是5左起的第一个小的数字，最终栈内数字为1，4，5。

算法，height是高度，用stack来维护一个单调递增的栈，这个栈只要遇到比自己小的数字就会把前面大的数字弹出，和上面的过程一样
只计算之前升序的长度
"""
class Solution:
    def largestRectangleArea(self, height):
        height.append(0)#在高度数组最后面加上一个0，这样原先的最后一个板子也可以被处理了。
        stack = [-1]
        ans = 0
        for i in range(len(height)):
#            print("height[i], height[stack[-1]]", height[i], height[stack[-1]])
            while height[i] < height[stack[-1]]:# 遇到高度递减直接出栈，开始计算面积
                h = height[stack.pop()]#当前最高高度
                w = i - stack[-1] - 1#其实可以看成是升序的序列长度
                ans = max(ans, h * w)
            stack.append(i)
#        height.pop()
        return ans, stack
if __name__ == "__main__":
    height = [2,1,5,6,2,3]
    height1 = [3,4,5]
    print(Solution().largestRectangleArea(height1))










