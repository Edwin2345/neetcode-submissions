class Solution:
    def jump(self, nums: List[int]) -> int:
        #keep a window of values you can jump to, until reach end
        #L,R are indices of window, both start at 0
        L, R =  0, 0
        
        minJumps = 0
        while R < len(nums) - 1:
            #find max reachable index (upperbound of window)
            maxReachableIndex = R
            for i in range(L,R+1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            #wasn't able to jump any further -> no solution
            if maxReachableIndex <= R:
               return -1
            
            #shift window and increment jump
            L = R + 1 #was able to jump at least 1 larger than window
            R = maxReachableIndex
            minJumps += 1
        
        return minJumps
        