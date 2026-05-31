"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #scan the line, keep track of max
        maxMeetingRoomsNeeded = 0
        timeline = []
        for i in intervals:
            timeline.append( (i.start,1) )
            timeline.append( (i.end,-1) )
        
        #sort timeline by time, then end before start for for same time value
        timeline.sort()

        cur = 0
        for time, change in timeline:
            cur += change
            maxMeetingRoomsNeeded = max(maxMeetingRoomsNeeded, cur)

        return maxMeetingRoomsNeeded
        
