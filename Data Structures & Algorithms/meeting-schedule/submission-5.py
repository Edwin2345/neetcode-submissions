"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    #sort the list by start time, then end time
    #iterate from start, if end time of prev is greater thans tart time of other, can't attend
    #O(nlogn) time
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort by start tiem first, then end time in assendign order
        intervals.sort(key=lambda x:(x.start,x.end))

        for i in range(0,len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
               return False

        return True 
