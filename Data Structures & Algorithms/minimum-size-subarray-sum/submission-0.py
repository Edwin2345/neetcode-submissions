class Solution:
    #slidign window, grow until we are equal then shift left
    #use vairable to save min size subarry
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSA = ""
        L, curSum = 0, 0
        for R in range(len(nums)):
            #add current num
            curSum += nums[R]

            #while we meet target, save and try to shrinl
            while curSum >= target:
                if minSA == "" or len(minSA) > R-L+1:
                   minSA = nums[L:R+1]

                curSum -= nums[L]
                L += 1 


        print(minSA)
        return len(minSA)