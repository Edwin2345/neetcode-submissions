class Solution:
    #consequtive sequence -> not necess in order, and cosneuqutive mans eahc num one greater than [rev]
    #sort nums to get consec nums beside eachother, ski
    # [2,3,4,4,5,10,20]
    def longestConsecutive(self, nums: List[int]) -> int:
        #base case
        if len(nums) == 0:
           return 0
            
        #sort to get numbers ordered ascendingly
        maxSeqLen = 0
        nums.sort()

        target = nums[0]
        streak = 0
        for i in range(len(nums)):
            #skip duplicate -. wont cotnrube to streak
            if i > 0 and nums[i] == nums[i-1]:
               continue

            #found target, update streak and target
            if nums[i] == target:  
               streak += 1
               target += 1
            #lost streak, next num not consequtive, restart seq here
            else:  
               streak = 1
               target = nums[i] + 1
            
            #udpate max seq len
            maxSeqLen = max(maxSeqLen, streak)

        return maxSeqLen

        