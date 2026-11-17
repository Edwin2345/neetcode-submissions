class Solution:
    # need to sort by start
    # single pass, while verlap detected update end time up
    #add the new interval with the updated end time
    # TC O(NlogN) for sorting, SC: O(1) extra space
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        i = 0
        mergedIntervals = []
        while i < len(intervals):
            curStart, curEnd = intervals[i]
            # check for overlaping intervals and update end time + index
            j = i + 1
            while j < len(intervals):
                nextStart, nextEnd = intervals[j]
                if curEnd < nextStart:
                   break
                curEnd = max(curEnd, nextEnd)
                j += 1
        
            # add the new merged interval and go to next
            mergedIntervals.append([curStart, curEnd])
            i = j

        return mergedIntervals
