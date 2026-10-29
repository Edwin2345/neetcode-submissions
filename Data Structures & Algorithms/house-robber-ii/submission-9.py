class Solution:
    # circular neighborhood, treat as two seperatew linear problems
    # 1: include first but skip last, 2: include last but skip first
    def rob(self, nums: List[int]) -> int:
        # edge case: only one house
        if len(nums) == 1:
            return nums[0]

        def calcMaxRob(i, houses):
            #base case: if i == len(house), max rob =0, if i == len-1, max rob = houses[i]
            maxRobs = [houses[-1], 0]

            for i in range(len(houses)-2, -1, -1):
                nextMaxRob = maxRobs[0]
                maxRobs[0] = max(houses[i] + maxRobs[1], nextMaxRob) 
                maxRobs[1] = nextMaxRob
            
            return maxRobs[0]

        max1 = calcMaxRob(0, nums[0 : len(nums) - 1])
        max2 = calcMaxRob(0, nums[1 : len(nums)])

        return max(max1, max2)
