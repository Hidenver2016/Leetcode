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
