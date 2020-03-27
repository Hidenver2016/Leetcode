# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 16:15:49 2020

@author: hjiang
"""

"""
利用一个范围在1~7的随机数产生器，构造一个范围在1～10的随机数产生器。
具体一点就是：

rand7()等概率地产生1,2,3,4,5,6,7.
rand7() - 1等概率地产生[0,6].
(rand7() - 1) *7等概率地产生0, 7, 14, 21, 28, 35, 42
(rand7() - 1) * 7 + (rand7() - 1)等概率地产生[0, 48]这49个数字
如果步骤4的结果大于等于40，那么就重复步骤4，直到产生的数小于40
把步骤5的结果mod 10 再加1， 就会等概率的随机生成[1, 10]
所以过程是：

rand7 --> rand49 --> rand40 --> rand10.
————————————————
版权声明：本文为CSDN博主「负雪明烛」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fuxuemingzhu/article/details/81809478
"""
class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        return self.rand40() % 10 + 1
        
    def rand49(self):
        """
        random integer in 0 ~ 48
        """
        return 7 * (rand7() - 1) + rand7() - 1
        
    def rand40(self):
        """
        random integer in 0 ~ 39
        """
        num = self.rand49()
        while num >= 40:
            num = self.rand49()
        return num