class Solution:
    # always a valid answer
    # brute force -->  TC: O(N^2) as for each indice, we check a path of at most N
    # SC: O(N) for call stack 
    # M = max(nums), N = len(nums)
    def jump(self, nums: List[int]) -> int:
        cache = {}
        def calcMinJumps(index):
            # overshot jump
            if index >= len(nums):
                return float("inf")
            # base case, already at last index
            if index == len(nums) - 1:
                return 0
            #already computed the min jumps at this index
            if index in cache:
               return cache[index] 

            # otherwise try all jumpValues and return min
            minJumps = float("inf")
            for jumpLen in range(1, nums[index] + 1):
                minJumps = min(minJumps, 1 + calcMinJumps(index + jumpLen))

            cache[index] = minJumps
            return cache[index]

        return calcMinJumps(0)
