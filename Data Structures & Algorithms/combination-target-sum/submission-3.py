class Solution:
    #all nums are positve, so if you go over end search
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        validCombos = []

        def genAllSums(curSumArr, targetSum, i):
            #base case: no valid solution
            if i >= len(nums) or targetSum < 0:
               return

            #foudn valid sum -> save a copy
            if targetSum == 0:
               validCombos.append(list(curSumArr))
               return

            #add current indice, and continue at same indice
            curSumArr.append(nums[i])
            targetSum -= nums[i]
            genAllSums(curSumArr, targetSum, i)

            #backtrack -> pop, skip and move to next index  
            curSumArr.pop()
            targetSum += nums[i]
            genAllSums(curSumArr, targetSum, i+1)

        genAllSums([],target,0)
        return validCombos
        