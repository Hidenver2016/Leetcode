# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 14:05:20 2018

@author: hjiang
"""

"""
Implement a MyCalendarTwo class to store your events. 
A new event can be added if adding the event will not cause a triple booking.

Your class will have one method, book(int start, int end). 
Formally, this represents a booking on the half open interval [start, end), 
the range of real numbers x such that start <= x < end.

A triple booking happens when three events have some non-empty intersection 
(ie., there is some time that is common to all 3 events.)

For each call to the method MyCalendar.book, 
return true if the event can be added to the calendar successfully without causing a triple booking. 
Otherwise, return false and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
Example 1:
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
Explanation: 
The first two events can be booked.  The third event can be double booked.
The fourth event (5, 15) can't be booked, because it would result in a triple booking.
The fifth event (5, 10) can be booked, as it does not use time 10 which is already double booked.
The sixth event (25, 55) can be booked, as the time in [25, 40) will be double booked with the third event;
the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.
Note:

The number of calls to MyCalendar.book per test case will be at most 1000.
In calls to MyCalendar.book(start, end), start and end are integers in the range [0, 10^9].
"""
"""

We store an array self.overlaps of intervals that are double booked, and self.calendar for intervals 
which have been single booked. 
We use the line start < j and end > i to check if the ranges [start, end) and [i, j) overlap.

The clever idea is we do not need to "clean up" ranges in calendar: if we have [1, 3] and [2, 4], 
this will be calendar = [[1,3],[2,4]] and overlaps = [[2,3]]. 
We don't need to spend time transforming the calendar to calendar = [[1,4]].
关键：没有预定的区域直接加在calendar, 一次预定的也加在calendar, 
而在calendar中，overlaps相当于二级标注，如果在overlaps里面有了，就表示不行了
"""

#Time (n^2)
class MyCalendarTwo:
    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        for i, j in self.overlaps: # i是start j是end
            if start < j and end > i:# 有overlaps，所以不行
                return False
        for i, j in self.calendar:
            if start < j and end > i:
                self.overlaps.append((max(start, i), min(end, j))) #更新overlap
        self.calendar.append((start, end)) # 更新calender
        return True
    
if __name__ == "__main__":
    T = MyCalendarTwo()
    print(T.book(10, 20))
    print(T.book(50, 60))
    print(T.book(10, 40))
    print(T.book(5, 15))
    print(T.book(5, 10))
    print(T.book(25, 55))
    
    

    