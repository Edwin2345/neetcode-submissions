class Solution:
    # hard to compute when circular but realize that first and last are connected
    # looking at linearly -> either skip the first node and include the last, or vice versa
    def rob(self, nums: List[int]) -> int:
        #edge case --> only one house, obviously rob it
        if len(nums) == 1:
           return nums[0] 

        def calcMaxRob(i, houses, cache):
            # past last house, max rob is 0
            if i == len(houses):
                return 0
            # already compute max rob
            if i in cache:
                return cache[i]
            # at last house max rob choice is to rob and go to end
            if i == len(houses) - 1:
                cache[i] = houses[-1] + calcMaxRob(i + 1, houses, cache)
                return cache[i]

            # otherwise, max of robing current or skiping to next
            cache[i] = max(
                houses[i] + calcMaxRob(i + 2, houses, cache), 
                calcMaxRob(i + 1, houses, cache)
            )
            return cache[i]

        # max rob in either you skip first hosue or the last house
        cache1, cache2 = {}, {}
        return max(
            calcMaxRob(0, nums[1:], cache1), 
            calcMaxRob(0, nums[0 : len(nums) - 1], cache2)
        )
