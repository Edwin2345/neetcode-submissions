class Solution:
    #1D DP Top Down: O(N^2) time as for first index -> check up to n-1 branchs, 2nd check up to n-2
    def jump(self, nums: List[int]) -> int:

        cache = {}
        def calcMinNumJumps(index):
            #base case: at last position need to take 0 jumps
            if index == len(nums) - 1:
               return 0 
            #alreazdy computed min num jumps
            if index in cache:
               return cache[index] 
            
            #otherwise, try taking 1 jump of size 1 to nums[index] to see if at end
            minNumJumps = float("inf")
            for j in range(1, nums[index]+1):
                newIndex = index + j
                #will jump out of bounds
                if newIndex >= len(nums):
                   break
                #otherwise, calculate min num of jumps by taking 1 jump of size j
                else:                                      
                   minNumJumps = min(minNumJumps, 1 + calcMinNumJumps(newIndex))
            
            cache[index] = minNumJumps
            return cache[index]
        
        return calcMinNumJumps(0)