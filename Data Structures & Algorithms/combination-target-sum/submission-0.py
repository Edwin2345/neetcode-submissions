class Solution:
    def helper(self, nums, i, target, curCombo, allCombos):
        #found valid combo
        if target == 0:
            allCombos.append(list(curCombo))
            return
        #current sum too large or end of list reached
        if target < 0 or i >= len(nums):
            return
        
        #option 1: append curent element once, and all ot it to be append aagain in future
        curCombo.append(nums[i])
        self.helper(nums, i, target-nums[i], curCombo, allCombos)

        #option 2: backtrack and skip current element
        curCombo.pop()
        self.helper(nums, i+1, target, curCombo, allCombos)



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #subsets, but allow for same element to be chosen again
        if target <= 0 or not nums:
            return []
        
        curCombo = []
        allCombos = []
        self.helper(nums, 0, target, curCombo, allCombos)
        return allCombos