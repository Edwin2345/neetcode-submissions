class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        allSums = []

        def dfs( i, curList, curSum ):
            #reached target sum
            if curSum == target:
               allSums.append( list(curList) ) 
               return
            # went over target sum -> dead end as all nums positive
            if curSum > target:
               return 
            #reach end of array
            if i == len(nums):
               return 
            
            #try adding current number and stay at current index
            curList.append( nums[i] )
            curSum += nums[i]
            dfs( i, curList, curSum )

            #backtrack -> remove current number and check next index
            curList.pop()
            curSum -= nums[i]
            dfs( i+1, curList, curSum )
        
        dfs(0, [], 0)
        return allSums
           







        return allSums