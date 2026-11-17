"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    #only way to have overalppign is if a meeting that starts earlier
    #ends after the next meeting starts
    # TC: O(nlogn) for soritng, SC: O(1) extra space
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #sort intervals based on start time, then end time
        intervals.sort(key=lambda x: (x.start, x.end))

        #check pairs of consecutive meeting for overlapp
        for i in range(0, len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
               return False

        return True 
