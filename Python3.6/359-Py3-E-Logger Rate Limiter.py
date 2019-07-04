# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 16:13:35 2019

@author: hjiang
"""

"""
Design a logger system that receive stream of messages along with its timestamps, 
each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), 
return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;
https://leetcode.com/problems/logger-rate-limiter/discuss/83294/Straight-forward-Python-solution
"""


    
class Logger(object):
    def __init__(self):
        self.d = {}

    def shouldPrintMessage(self, timestamp, message):
        if message in self.d and timestamp - self.d[message] < 10:
            return False
        else:
            self.d[message] = timestamp
            return True