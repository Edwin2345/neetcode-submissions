class Solution:
    # bottom up. max rob at ith house depends on the max rob of i+1 and i+2 house
    #O(n) TC, O(1) space)
    def rob(self, nums: List[int]) -> int:
        # base case: at house i == len(nums), max rob is 0, at i == len(nums) -1 max rob is nums[i]
        maxRob = [nums[-1], 0]

        for i in range(len(nums) - 2, -1, -1):
            nextHouseMax = maxRob[0]
            maxRob[0] = max(nums[i] + maxRob[1], maxRob[0])
            maxRob[1] = nextHouseMax

        return maxRob[0]
