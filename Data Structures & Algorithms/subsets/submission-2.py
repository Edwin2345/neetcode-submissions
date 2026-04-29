class Solution:
    def helper(self, nums, i, curSet, allSets):
        #passed through nums -> append a copy of the subset result and stop
        if i >= len(nums):
            allSets.append(list(curSet))
            return
        
        #create a subset that takes ith element
        curSet.append(nums[i])
        self.helper(nums, i+1, curSet, allSets)

        #backtrack -> remove ith elemtn and create subset without it
        curSet.pop()
        self.helper(nums, i+1, curSet, allSets)
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        allSets = []
        curSet = []
        self.helper(nums, 0, curSet, allSets)
        return allSets