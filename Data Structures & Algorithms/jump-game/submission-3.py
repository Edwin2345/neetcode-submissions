class Solution:
    #Q: does it have to exactly be last index or can you go over

    # O(N) Time, O(N) Space approach -> bfs with queue + visited set
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])
        visit = set([0])

        while len(q) > 0:
            #check if curr index is at end
            i = q.popleft()
            if i == len(nums) - 1:
               return True
            
            #add all reachable indices to queue
            for j in range(1, nums[i] + 1):
                newIndex = i + j
                if newIndex >= len(nums):
                   break
                elif newIndex not in visit:
                   q.append( newIndex ) 
                   visit.add( newIndex )

        return False 
        