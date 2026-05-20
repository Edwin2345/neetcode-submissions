"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #sort based on start times
        intervals.sort(key=lambda x: x.start)

        #use min heap to add all end times, and only pop from heap
        # if the next concetuive interval starts after min end
        #otherwise, add that end tiem to heap
        min_heap = []
        for interval in intervals:
            #next internval has no overlap, can use same room
            if min_heap and min_heap[0] <= interval.start:
               heapq.heappop(min_heap)

            heapq.heappush(min_heap, interval.end) 

        return len(min_heap)