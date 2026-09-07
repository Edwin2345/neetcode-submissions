class Solution:
    #Greedy: at each local index consider the max range of indics you can jump to (levels)
    #Maintian levels using L,R pointers
    def jump(self, nums: List[int]) -> int:
        L, R = 0, 0
        numJumps = 0
        while R < len(nums) - 1:
            #find the furthest jumpable index within this level
            maxReachableIndex = R
            for i in range(L, R+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            #take one jump, shifting to next level
            L = R            
            R = maxReachableIndex
            numJumps += 1
        
        return numJumps
      

            
        
        