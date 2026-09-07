class Solution:
    # O(N) Time, O(1) Space  -> greedy:
    #at each index check if > maxReachableIndex -> if so can't reach end
    #otherwise compute the maxReachableIndex at that local index, and see if >= last index
    def canJump(self, nums: List[int]) -> bool:
        maxReachableIndex = 0

        for i in range(len(nums)):
            #can't reach current index from the prev's maxReachable ->  can't jump to end
            if i > maxReachableIndex:
               return False 
            
            #update maxReachableIndex using this current index
            maxReachableIndex = max(maxReachableIndex, i + nums[i])

        #was able to jump to last index
        return True
        