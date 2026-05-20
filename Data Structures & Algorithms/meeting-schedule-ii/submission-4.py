"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sweep the line: take every sinle start and end point
        #and sort that, but add +1 for every start (as need room), and -1 to end as nolonger need
        #max value of cumulate sorted sum is number of rooms

        points = []
        for i in intervals:
            points.append( (i.start,1) )
            points.append( (i.end,-1) )

        #sort by both point and assigned value to ensure we end before we start
        #that way maxROoms doesn't incorrectly record (0,8) (8,10) as 2 instead of 1
        points.sort(key=lambda x: (x[0], x[1]))

        maxRooms = 0
        sum = 0
        for point in points:
            sum += point[1]
            maxRooms = max(maxRooms, sum)

        return maxRooms
        
       