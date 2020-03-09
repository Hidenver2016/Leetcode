# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:48:31 2020

@author: hjiang
"""

"""
Longest sub-array having sum k
Given an array arr[] of size n containing integers. 
The problem is to find the length of the longest sub-array having sum equal to the given value k.

Examples:

Input : arr[] = { 10, 5, 2, 7, 1, 9 }, 
            k = 15
Output : 4
The sub-array is {5, 2, 7, 1}.

Input : arr[] = {-5, 8, -14, 2, 4, 12},
            k = -5
Output : 5


Efficient Approach: Following are the steps:

Initialize sum = 0 and maxLen = 0.
Create a hash table having (sum, index) tuples.
For i = 0 to n-1, perform the following steps:
Accumulate arr[i] to sum.
If sum == k, update maxLen = i+1.
Check whether sum is present in the hash table or not. If not present, then add it to the hash table as (sum, i) pair.
Check if (sum-k) is present in the hash table or not. If present, then obtain index of (sum-k) from the hash table as index. 
Now check if maxLen < (i-index), then update maxLen = (i-index).
Return maxLen.
"""

# Python3 implementation to find the length 
# of longest subArray having sum k 
  
# function to find the longest 
# subarray having sum k 
def lenOfLongSubarr(arr, n, k): 
  
    # dictionary mydict implemented 
    # as hash map 
    mydict = dict() 
  
    # Initialize sum and maxLen with 0 
    sum = 0
    maxLen = 0
  
    # traverse the given array 
    for i in range(n): 
  
        # accumulate the sum 
        sum += arr[i] 
  
        # when subArray starts from index '0' 
        if (sum == k): 
            maxLen = i + 1
  
        # check if 'sum-k' is present in 
        # mydict or not 
        elif (sum - k) in mydict: #注意这个是关键，意味着中间序列有可能有符合要求的
            maxLen = max(maxLen, i - mydict[sum - k]) 
  
        # if sum is not present in dictionary 
        # push it in the dictionary with its index 
        if sum not in mydict: 
            mydict[sum] = i 
  
    return maxLen 
  
# Driver Code 
if __name__ == '__main__': 
    arr = [10, 5, 2, 7, 1, 9] 
    n = len(arr) 
    k = 10
    print("Length =", lenOfLongSubarr(arr, n, k)) 
  
# This code is contributed by  
# chaudhary_19 (Mayank Chaudhary) 