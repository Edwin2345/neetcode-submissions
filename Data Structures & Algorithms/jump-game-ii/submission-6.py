class Solution:
    #Greedy: consider the max range of indices you can reach given the current range of idncies
    #keep trakc of this range with L, R points
    def jump(self, nums: List[int]) -> int:
        L,R = 0,0

        numJumps = 0
        while R < len(nums) - 1:
            #find max reachable index -> upperbound of next level
            maxReachableIndex = R
            for i in range(L,R+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            #can't jump any further -> infinit jumps to top
            if R + 1 > maxReachableIndex:
               return float('inf')

            #shift to next level and make 1 jump
            L = R + 1
            R = maxReachableIndex
            numJumps += 1
        
        return numJumps
        