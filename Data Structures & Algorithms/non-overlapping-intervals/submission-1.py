class Solution:
    #[1,4] [1,3], [2,3], [4,5] [5,6]
    #idea: sort by start time, keep trak of endTime
    #if we encounter an overlap, we take the minum end time
    #this effectly removes the interval with later end time so we increment remove count by 1
    #greedy approach: we take the sooner finishing interval as its less likely we will collide
    #if no coluison, we just update
    #at least 1 interval and startI < endi
    #[1,2],[1,4],[1,3],[2,4]
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort by start times
        intervals.sort(key=lambda x:x[0])

        prevEndTime = intervals[0][1]
        numIntervalsRemoved = 0

        for i in range(1, len(intervals)):
            curStartTime, curEndTime = intervals[i]
            #overlapping intervals -> remove the later ending interval
            if prevEndTime > curStartTime:
               prevEndTime = min(prevEndTime, curEndTime)
               numIntervalsRemoved += 1
            #no overlap, just update prevEnd for next interation
            else:
               prevEndTime = curEndTime

        return numIntervalsRemoved
        
        