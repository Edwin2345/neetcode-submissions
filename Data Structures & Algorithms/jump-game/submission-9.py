class Solution:
    #greedy approach: at each level keep a range of jumpable indicies with L and R pointers
    #range is from L=R+1 to R=maxReachableIndice
    #O(N) Time, O(1) Space
    def canJump(self, nums: List[int]) -> bool:
        L,R = 0,0

        while R < len(nums) - 1:
            #find max reachable indice at curent level
            maxReachableIndex = R
            for i in range(L,R+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            #if we are unable to jump further -> return false
            if R + 1 > maxReachableIndex:
               return False

            #go to next level
            L = R + 1
            R = maxReachableIndex

        #able to reach last index
        return True 


        