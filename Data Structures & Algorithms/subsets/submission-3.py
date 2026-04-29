class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSubsets = []
        curSubset = []

        def dfs(i):
            #add completed supset
            if i == len(nums):
                allSubsets.append(list(curSubset))
                return
            
            #decision to include ith element
            curSubset.append(nums[i])
            dfs(i+1)

            #backtrack and skip ith element
            curSubset.pop()
            dfs(i+1)
            
        dfs(0)
        return allSubsets