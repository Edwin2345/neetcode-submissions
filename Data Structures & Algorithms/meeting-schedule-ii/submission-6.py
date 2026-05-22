"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #use a min heap, max heap size is num of rooms
        #pop from heap if cur.startTIme > end time in heap
        intervals.sort(key=lambda x: x.start)
    
        min_heap = []
        for intvl in intervals:
            if min_heap and min_heap[0] <= intvl.start:
               heapq.heappop(min_heap)

            heapq.heappush(min_heap, intvl.end)                   

        return len(min_heap)