"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #map each start time to +1 (as room needed) and end time to -1 (room no logner needed)
        timePoints = []
        for interval in intervals:
            timePoints.append( (interval.start, +1))
            timePoints.append( (interval.end, -1) )
        
        #sort ascending both time then value 
        #(as we want to end before start since (A,B) (B,C) is NOT conflict) 
        timePoints.sort()

        #sum the +/- 1 values 
        #max value at any point in time is min number of rums to schedule meeting
        minNumRooms = 0
        curSum = 0
        for tp in timePoints:
            curSum += tp[1]
            minNumRooms = max(minNumRooms, curSum)
            
        return minNumRooms
        