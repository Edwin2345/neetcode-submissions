"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    # we no a peronc can't attend a meetign if there is any conflict
    # conflict -> preceeding meeting ends after current meeting starts
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort meetings by start times
        intervals.sort(key=lambda x: x.start)

        #check successive meeitng pairs
        for i in range(1,len(intervals)):
            #previous meeting ends after current starts
            if intervals[i-1].end > intervals[i].start:
               return False 

        #no conflicts found
        return True
