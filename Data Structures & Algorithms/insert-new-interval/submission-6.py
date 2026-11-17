class Solution:
    #insert the interval then run merge algo
    # current intevals is intially sorted ascendign roder by start time
    # TC: O(n) to insert and merge, SC: O(1) extra space
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
          
        #insert new inteval based on start time
        #append at end and then bubble down
        intervals.append(newInterval)
        i = len(intervals) - 1
        while i > 0:
           #interval in correct spot based on start time
           if intervals[i][0] >= intervals[i-1][0]:
              break
           #otherwise swap the two
           intervals[i], intervals[i-1] = intervals[i-1], intervals[i]
           i -= 1
            
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


        
        