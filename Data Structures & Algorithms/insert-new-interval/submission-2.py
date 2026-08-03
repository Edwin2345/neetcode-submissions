class Solution:
    #insert newInterval by lookign at the start time (as intervals initally sorted)
    #then run merge algo
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #Insert New Interval
        #empty set of intervals
        if len(intervals) == 0:
           intervals.append(newInterval)
        #else, linear travers to find spot
        else:
            foundSpot = False
            for i in range(len(intervals)):
                if newInterval[0] <= intervals[i][0]:
                   intervals.insert(i, newInterval)
                   foundSport = True

            #add at end as larger than everythign else
            if not foundSpot:
               intervals.append(newInterval)     
        
        #merge overlapping intervals
        mergedIntervals = []
        i = 0
        while i < len(intervals):
            curStartTime, curEndTime = intervals[i][0], intervals[i][1]

            j = i + 1
            while j < len(intervals) and curEndTime >= intervals[j][0]:
                  curEndTime = max(curEndTime, intervals[j][1])
                  j += 1
            
            mergedIntervals.append([curStartTime, curEndTime])
            i = j

        return mergedIntervals
        

