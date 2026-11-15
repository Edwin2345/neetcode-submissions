class Solution:
    # at least one num and values are non-neg
    # brute force attempt -> recursive func
    # TC: O(N) as we compute each index once, SC: O(N) for call stack where N is len(nums), M is max(nums)
    def canJump(self, nums: List[int]) -> bool:
        cache = {}
        def canJumpToEnd(index):
            # reached end
            if index == len(nums) - 1:
                return True
            # jumped past end --> call it false
            if index >= len(nums):
                return False
            #already computed if you can jump to end
            if index in cache:
               return cache[index] 

            # otherwise, try to jump every possible amount
            for jump in range(1, nums[index] + 1):
                if canJumpToEnd(index + jump):
                    cache[index] = True
                    return cache[index]

            cache[index] = False
            return cache[index]
        
        return canJumpToEnd(0)
