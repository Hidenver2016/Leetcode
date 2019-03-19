# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 14:22:33 2019

@author: hjiang
"""

"""
https://leetcode.com/problems/number-of-digit-one/discuss/64390/AC-short-Java-solution
public int countDigitOne(int n) {
  int count = 0;
    
  for (long k = 1; k <= n; k *= 10) {
    long r = n / k, m = n % k;
    // sum up the count of ones on every place k
    count += (r + 8) / 10 * k + (r % 10 == 1 ? m + 1 : 0);
  }
    
  return count;
}

1. 每十个数，个位为1的，只有1个，所以是(n//k)//10 （计算有多少个十）, 如果是个位, k=1, (例如 50， 就有 (50//1)//10 = 5， 5 个 1 （在各位） 
如果是十位， k=10 （对应100用的）.
而对于100以内，有10个1，在十位上的， 所以计算十位上的1，就是数多少个100. 此时k=10, 就是(n//k)//10*k
设r = n//k, 那么就是
r//10*k

2. 现在我们考虑特殊行，就是10～19
对于10， （n/1）/10*1 = 1,是有一个1在个位上，我们还需要看看 m = n % k, 这时十位上的1的个数就是 m+1
所以上面的公式变为：
r // 10 * k + (r % 10 == 1? m+1 ： 0)

3. 等一下，还有20， 21， 22
（20//10）//10*10 + (r % 10 == 1 ? m + 1 : 0) = 0, 20用上面的方法算是错误的， 计算十位的1的个数
对于这些数就是需要+8来判断一下，因为这些数都是20以上的，自然包括了那些10～19的1
(r + 8) // 10 * k + (r % 10 == 1 ? m + 1 : 0)

（20//10 + 8）//10*10 + (r % 10 == 1 ? m + 1 : 0) = 10, 改一个+8就好了




"""
class Solution:
    def countDigitOne(self, n):
        k = 1
        count = 0
        while k <= n:
            r = n // k
            m = n % k
            h =  m + 1 if r % 10 == 1 else 0
            count += (r + 8) // 10 * k + h
            k *= 10
            
        return count
            


    
class Solution1:
    def countDigitOne(self, n):
        res, a, b = 0, 1, 1
        while n > 0:
            res += (n + 8) // 10 * a + (n % 10 == 1) * b
            b += n % 10 * a
            a *= 10
            n //= 10            
        return res
    
    
if __name__ == "__main__":
    print(Solution().countDigitOne(13))