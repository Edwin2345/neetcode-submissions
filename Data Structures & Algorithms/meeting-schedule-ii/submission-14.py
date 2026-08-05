"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # O(N) O(N) solution SCAN THE LINE -> map start times to +1, end times to -1
    #sort the line points by time, and then mapped value (start before end)
    #iterate throguh points, cnt += mapped value --> roomsNeeds = max of cnt as multiple
    #meeytings that overalp (start before meeting ends) must be in sep rooms
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #map time points to +1 for start, -1 for end sort 
        timeline = []
        for t in intervals:
            timeline.append( (t.start, 1) )
            timeline.append( (t.end, -1) )
        
        #sort by time ascending, then mapped value ascendign so ends piont procesed before start
        timeline.sort(key=lambda x:(x[0], x[1]))

        #iterate through sorted points, and scan line 
        roomsNeeded = 0
        curSum = 0
        for time, mappedVal in timeline:
            curSum += mappedVal
            roomsNeeded = max(roomsNeeded, curSum)
 
        return roomsNeeded
        