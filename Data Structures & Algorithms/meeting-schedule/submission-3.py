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

         #check if previous end time is after current start time
         for i in range(len(intervals)-1, 0, -1):
             if intervals[i].start < intervals[i-1].end:
                return False
        
         return True

