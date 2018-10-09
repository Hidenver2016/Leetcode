# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 15:31:16 2018

@author: hjiang
"""
'''
#Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
#
#Examples:
#
#s = "leetcode"
#return 0.
#
#s = "loveleetcode",
#return 2.
'''
def solution(nums):
# 注意 本来是len(nums)-1,  但是range本来只到len(nums)-1, 所以直接写成range(len(nums))
# 但是考虑到对于最后一个字母，不可能再和之后的比较了，所以直接把字长取在len(nums)-1,比较到倒数第二个为止    
    for i in range(len(nums)-1): 
        sign = 0
        for j in range(i+1, len(nums)):# 必须是和之后的比较所以是i+1
            if nums[i] == nums[j]:
                sign += 1
        if sign == 0:
            return i
        
    return -1


def solution1(nums):
    
    letters = {}
    for c in nums:
        if c in letters:
            letters[c] = letters[c] + 1
        else:
            letters[c] = 1
            
    for i in range(len(nums)):
        if letters[nums[i]] == 1:
            return i
        
    return -1

# 这个最巧妙
def solution2(nums): 
    letters = "abcdefghijklmnopqrstuvwxyz"
    index1 = [nums.index(l) for l in letters if nums.count(l) == 1]
    return min(index1) if len(index1) > 0 else -1

        

if __name__ == "__main__":
    print(solution2('loveleetcode'))          
            

        