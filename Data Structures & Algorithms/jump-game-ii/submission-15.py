class Solution:
    # always a valid answer, always non neg
    # Optimization: do a bfs like approach and track the range of indicies you cna jump to
    # TC: O(N) as single scane, SC: O(1) as just 1 poitner vaiables
    def jump(self, nums: List[int]) -> int:
        minJumps = 0
        minReachableIndex, maxReachableIndex = 0,0

        while maxReachableIndex < len(nums) - 1:
            #update max reachable by checking all values in range
            oldMaxReachableIndex = maxReachableIndex
            for i in range(minReachableIndex, maxReachableIndex + 1):
                maxReachableIndex = max(maxReachableIndex, i + nums[i])
            
            #could not jump any futurer
            if oldMaxReachableIndex == maxReachableIndex:
               return -1
            
            #increment jumps and shift min index to next level
            minJumps += 1
            minReachableIndex = oldMaxReachableIndex + 1

        return minJumps
        
