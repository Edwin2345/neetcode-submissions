class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        allCombos = []
        curCombo = []

        def dfs(i,curSum):
            #edge case -> curSum larger than target, array oob 
            if i >= len(nums) or curSum > target:
                return
            #found a valid combo sum
            if curSum == target:
                allCombos.append(list(curCombo))
                return
            
            #take ith element (can take again)
            curCombo.append(nums[i])
            curSum += nums[i]
            dfs(i,curSum)

            #backtrack and skip ith element
            curCombo.pop()
            curSum -= nums[i]
            dfs(i+1,curSum)


        dfs(0,0)
        return allCombos