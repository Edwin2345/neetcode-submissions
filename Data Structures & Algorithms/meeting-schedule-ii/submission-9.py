"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #convert each start and end time into points
        points = []
        for i in intervals:
            points.append( (i.start,1) )
            points.append( (i.end,-1) )
        
        points.sort()

        #keep max suma s meeting rooms
        numRooms = 0
        curSum = 0
        for p in points:
            curSum += p[1]
            numRooms = max(numRooms, curSum)
        
        return numRooms
