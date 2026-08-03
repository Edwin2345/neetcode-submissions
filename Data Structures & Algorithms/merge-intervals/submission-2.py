class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #sort the intervals by start date, for each interval
        #if next inteval start date is less than or equal to prev end datr, juadjust the end tiem boundary -> add finalized merged intevals

        intervals.sort(key=lambda x:x[0])

        mergedIntervals = []
        i = 0
        while i < len(intervals):
            #get start and end tomes of ith interval
            ithStartTime, ithEndTime = intervals[i][0], intervals[i][1]

            #merge intervals that overlap with ith interval 
            #they start before or when ith ends
            j = i + 1
            while j < len(intervals) and ithEndTime >= intervals[j][0]:
                  ithEndTime = max(ithEndTime, intervals[j][1])
                  j += 1
            
            #add merged interval
            mergedIntervals.append([ithStartTime, ithEndTime])
            i = j
           
        return mergedIntervals