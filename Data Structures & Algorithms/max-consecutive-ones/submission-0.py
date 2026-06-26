class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        curr_ones = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr_ones += 1

            if nums[i] == 0 or i == len(nums) - 1:
                if curr_ones > max_ones:
                    max_ones = curr_ones
                    
                curr_ones = 0
        
        return max_ones
            