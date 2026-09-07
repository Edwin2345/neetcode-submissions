class Solution:
    #bfs apporach
    def canJump(self, nums: List[int]) -> bool:
        q = deque([0])
        visit = set([0])

        while len(q) > 0:
            #check if reached last index
            i = q.popleft()
            if i == len(nums)-1:
               return True 
            
            #otherwise, add unexplored reachable indicies
            for j in range(1, nums[i] + 1):
                newIndex = i + j
                if newIndex > len(nums) - 1:
                   break
                elif newIndex not in visit:
                    q.append(newIndex)
                    visit.add(newIndex) 

        return False 
        