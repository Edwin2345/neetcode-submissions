"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

        1,2,3,4
          2,3
        
        1,2,3,4
        1,3
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #brute force
        for i in range(len(intervals)):
            for j in range(i+1, len(intervals)):
                m1 = intervals[i]
                m2 = intervals[j]
                #check if valid combo:
                if m2.start >= m1.end or m1.start >= m2.end:
                    continue
                return False               
        return True