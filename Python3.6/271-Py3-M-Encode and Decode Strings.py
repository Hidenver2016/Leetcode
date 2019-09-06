# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 15:56:49 2019

@author: hjiang
"""

"""
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

 

Note:

The string may contain any possible characters out of 256 valid ascii characters. 
Your algorithm should be generalized enough to work on any possible characters.

Do not use class member/global/static variables to store states. 
Your encode and decode algorithms should be stateless.

Do not rely on any library method such as eval or serialize methods. 
You should implement your own encode/decode algorithm.
https://blog.csdn.net/fuxuemingzhu/article/details/79264976
这个题是个佛性题。不给任何要求，只要能编码、解码出来就行。
"""

class Codec:
    def __init__(self):
        self.count = 0
        self.d = dict()
    
    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.count += 1
        self.d[self.count] = longUrl
        return str(self.count)

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.d[int(shortUrl)]
#https://leetcode.com/problems/encode-and-decode-strings/discuss/70448/1%2B7-lines-Python-(length-prefixes)    
class Codec1:

    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs
class Codec2:
    def encode(self, strs):
        result = []
        for i in range(len(strs)):
            result.append((strs[i]))
        return result

    def decode(self, strs):
        result = []
        for i in range(len(strs)):
            result.append((strs[i]))
        return result
    

if __name__ == "__main__":
    e = Codec2().encode(["Hello","World"])
    print(e)
    print(Codec2().decode(e))
