class Solution:
    #consequtive sequence -> not necess in order, and cosneuqutive mans eahc num one greater than [rev]
    #sort nums to get consec nums beside eachother, ski
    # [2,3,4,4,5,10,20]
    #TC: O(N) as we only check beiging of streaks and scan eahc num once, SC O(N) for set
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeqLen = 0

        # O(N) scan of streak
        for n in nums:
            #not the beging of a seq (smaller conseq exists), skip
            if n-1 in numSet:
               continue

            #otherwise find longest conseq seq beign at this num
            target = n
            streak = 0
            while target in numSet:
                streak += 1
                maxSeqLen = max(maxSeqLen, streak)
                target += 1

        return maxSeqLen

        