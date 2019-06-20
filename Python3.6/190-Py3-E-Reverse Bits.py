# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 11:31:35 2019

@author: hjiang
"""

"""
Reverse bits of a given 32 bits unsigned integer.

 

Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, 
so return 3221225471 which its binary representation is 10101111110010110010011101101001.
 

Note:

Note that in some languages such as Java, there is no unsigned integer type. 
In this case, both input and output will be given as signed integer type and should not affect your implementation, 
as the internal binary representation of the integer is the same whether it is signed or unsigned.
In Java, the compiler represents the signed integers using 2's complement notation. 
Therefore, in Example 2 above the input represents the signed integer -3 and 
the output represents the signed integer -1073741825.
 

Follow up:

If this function is called many times, how would you optimize it?
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bins = bin(n)[2:][::-1]#先把数字变成2进制，比如bin(7) 等于 '0b111',然后取后面的数字[2:],然后翻转
        rev = (bins + '0' * (32 - len(bins)))#一定要是32位的二进制表示才行，因此一定要进行补全。
        return int(rev, 2)
