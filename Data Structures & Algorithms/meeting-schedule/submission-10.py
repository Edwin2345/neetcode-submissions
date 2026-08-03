"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort by starting date
        intervals.sort(key=lambda x:x.start)

        for i in range(len(intervals)-1):
            #can't attend if the prev meeting ends after the next starts
            if intervals[i].end > intervals[i+1].start:
               return False

        return True 