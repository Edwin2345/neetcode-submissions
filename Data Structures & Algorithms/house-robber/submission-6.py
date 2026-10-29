class Solution:
    #approach one: top down with recusrive decision func
    def rob(self, nums: List[int]) -> int:

        cache = {}
        def calcMaxRob(i):
            #finished scanning neighborhood
            if i == len(nums):
               return 0 
            # at the last house, only choice is to rob and go to end
            if i == len(nums) - 1:
               return nums[i] 
            #already computed
            if i in cache:
               return cache[i]
            
            #otherwise, max rob amount from this house onwards
            #is the max between robbing current house and going i+2 or skiping and going i+1
            cache[i] = max(nums[i] + calcMaxRob(i+2), calcMaxRob(i+1))
            return cache[i]
        
        return calcMaxRob(0)