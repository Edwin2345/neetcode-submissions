class Solution:
    def rob(self, nums: List[int]) -> int:
        #make decision at each house to take current and go next next or skip and go next
        #Top Down: cache the max rob amount at each house
        cache = {}
        def maxRobAmount(house):
            if house >= len(nums):
               return 0
            if house in cache:
               return cache[house]  
            
            cache[house] = max(maxRobAmount(house + 1), nums[house] + maxRobAmount(house + 2)) 
            return cache[house]
        
        return maxRobAmount(0)