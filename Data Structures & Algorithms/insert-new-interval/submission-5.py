class Solution:
    #insert the interval then run merge algo
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
          
        #append new interval then sort entire list by start time
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x[0])

        #merge overlapping intervals
        mergedIntervals = []
        i = 0
        while i < len(intervals):
            curStart, curEnd = intervals[i]
            #while overlappign, update end time of merged interval
            j = i + 1
            while j < len(intervals):
                nextStart, nextEnd = intervals[j]
                if curEnd < nextStart:
                   break
                curEnd = max(curEnd, nextEnd)
                j += 1
            
            #save merged interval and go to next index
            mergedIntervals.append( [curStart, curEnd] )
            i = j

        return mergedIntervals


        
        