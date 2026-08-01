class Solution:
     #time: o(NLOGN) for sorting, space: O(N) for merged output
     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort array by start
        intervals.sort(key=lambda x: x[0])
        mergedIntervals = []

        i=0
        while i < len(intervals):
            curStart = intervals[i][0]
            curEnd  = intervals[i][1]

            #merge all proceeding intervals that overlap with this, (start before other ends)
            #extend the end of the current interval
            j = i+1
            while j < len(intervals) and intervals[j][0] <= curEnd:
                curEnd = max(curEnd, intervals[j][1])
                j += 1

            #add merged interval
            i = j
            mergedIntervals.append( [curStart, curEnd])

        return mergedIntervals



        


        