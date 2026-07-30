"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    #brute force: compare every meeting to see if conflict
    #conflict if a meeting starts another ends and ends after the other starts
    #comapre every pair to get fair assemtn

    # i1:   S --- E
    # i2:     S -- - E

    # or 
    # i1:   S -- E
    # i2:   S -E

    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
      
        for i1 in intervals:
            for i2 in intervals:
                #don't comapre the same meeting
                if i1 == i2:
                   continue 
                if i1.start <= i2.start and i1.end > i2.start:
                   return False 
         
        return True