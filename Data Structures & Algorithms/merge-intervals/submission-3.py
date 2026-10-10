class Solution:
    #sort by start times to 
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort intervals by start time
        intervals.sort(key=lambda x:x[0])

        mergedIntervals = []
        i = 0
        #iterate through intervals
        while i < len(intervals):
            iStart, iEnd = intervals[i]
            #check all succeeding interval
            j = i + 1
            while j < len(intervals):
                jStart, jEnd = intervals[j]
                #next interval not overlapping, break off and start new interval
                if iEnd < jStart:
                   break
                #otherwise, take the max of the 2 ends for the new merged interval and compare with next meeting
                iEnd = max(iEnd, jEnd) 
                j += 1
            
            #add merged interval and move i pointer to j
            mergedIntervals.append( [iStart, iEnd] )
            i = j
        
        return mergedIntervals
