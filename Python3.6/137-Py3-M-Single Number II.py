# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:32:52 2019

@author: hjiang
"""

"""
Given a non-empty array of integers, every element appears three times except for one, 
which appears exactly once. Find that single one.

Note

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

用3个整数来表示INT的各位的出现次数情况，one表示出现了1次，two表示出现了2次。当出现3次的时候该位清零。最后答案就是one的值。

ones   代表第ith 位只出现一次的掩码变量
twos  代表第ith 位只出现两次次的掩码变量
threes  代表第ith 位只出现三次的掩码变量
假设现在有一个数字1，那么我们更新one的方法就是‘亦或’这个1，则one就变成了1，而two的更新方法是用上一个状态下的one去‘与’上数字1，
然后‘或’上这个结果，这样假如之前one是1，那么此时two也会变成1，这make sense，因为说明是当前位遇到两个1了；反之如果之前one是0，
那么现在two也就是0。注意更新的顺序是先更新two，再更新one，不理解的话只要带个只有一个数字1的输入数组看一下就不难理解了。
然后我们更新three，如果此时one和two都是1了，那么由于我们先更新的two，再更新的one，two为1，说明此时至少有两个数字1了，
而此时one为1，说明了此时已经有了三个数字1，这块要仔细想清楚，因为one是要‘亦或’一个1的，值能为1，说明之前one为0，
实际情况是，当第二个1来的时候，two先更新为1，此时one再更新为0，下面three就是0了，那么‘与’上three的相反数1不会改变one和two的值；
那么当第三个1来的时候，two还是1，此时one就更新为1了，那么three就更新为1了，此时就要清空one和two了，让它们‘与’上three的相反数0即可，
最终结果将会保存在one中，参见代码如下：

https://www.cnblogs.com/grandyang/p/4263927.html 
"""
class Solution2(object):
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        one, two, carry = 0, 0, 0
        for x in A:
            two |= one & x
            one ^= x
            carry = one & two
            one &= ~carry
            two &= ~carry
        return one