class Solution:
    def rob(self, nums: List[int]) -> int:
        #make decision at each house to take current and go next next or skip and go next
        
        #Bottom up: use the max rob amount of the next, and next next house to compute current
        #base cases: index 1 is past last house, index 0 is at last house
        nextMaxRobAmounts = [nums[-1],0]

        for houseNum in range(len(nums)-2,-1,-1):
            nextMaxRob = nextMaxRobAmounts[0]
            nextMaxRobAmounts[0] = max( nums[houseNum] + nextMaxRobAmounts[1],  nextMaxRobAmounts[0])
            nextMaxRobAmounts[1] = nextMaxRob
                   
        return nextMaxRobAmounts[0]