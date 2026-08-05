"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    # O(NLOGN) O(N) solution SCAN THE LINE -> map start times to +1, end times to -1
    #sort the line points by time, and then mapped value (start before end)
    #iterate throguh points, activeMeetings += mappedValue, roomsNeeded = max(roomsNeeds, activeMeetging)
    #acive meetigns tells us how many meeting have started and/or are proceeding at a given time point, when meeitng ends we shink
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #map time points to +1 for start, -1 for end sort 
        timeline = []
        for t in intervals:
            timeline.append( (t.start, 1) )
            timeline.append( (t.end, -1) )
        
        #sort by time ascending, then mapped value ascendign so ends piont procesed before start
        timeline.sort(key=lambda x:(x[0], x[1]))

        #iterate through sorted points, and scan line to find how many active meetings at each TP
        #acive meetigns tells us how many meeting have started and/or are proceeding at a given time point, when meeitng ends we shin
        roomsNeeded = 0
        activeMeetings = 0
        for time, mappedVal in timeline:
            activeMeetings += mappedVal
            roomsNeeded = max(roomsNeeded, activeMeetings)
 
        return roomsNeeded
        