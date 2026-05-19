"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
         #sort meetings by start time
         intervals.sort(key=lambda x: x.start)

         #for each neighboring meeting, check if prev end time > cur start time
         for i in range(len(intervals)-1):
             if intervals[i+1].start < intervals[i].end:
                return False
         
         return True