class Solution:
    # circular neighborhood, treat as two seperatew linear problems
    # 1: include first but skip last, 2: include last but skip first
    def rob(self, nums: List[int]) -> int:
        # edge case: only one house
        if len(nums) == 1:
            return nums[0]

        cache = {}

        def calcMaxRob(i, houses):
            if i == len(houses):
                return 0
            if i == len(houses) - 1:
                return houses[i]
            if i in cache:
                return cache[i]

            cache[i] = max(houses[i] + calcMaxRob(i + 2, houses), calcMaxRob(i + 1, houses))
            return cache[i]

        max1 = calcMaxRob(0, nums[0 : len(nums) - 1])
        cache.clear()
        max2 = calcMaxRob(0, nums[1 : len(nums)])

        return max(max1, max2)
