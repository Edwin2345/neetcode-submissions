class Solution:
    def helper(self, candidates, i, curList, curSum, target, validSumList):
        #found valid combination
        if curSum == target:
            validSumList.append(list(curList))
            return
        #index out of bounds
        if i >= len(candidates):
            return

        #take the ith element in the list
        curList.append(candidates[i])
        curSum += candidates[i]
        self.helper(candidates, i+1, curList, curSum, target, validSumList)

        #backtrack and try not taking ith element -> skip all duplicates
        curList.pop()
        while(i+1 < len(candidates) and candidates[i] == candidates[i+1]):
             i += 1
        curSum -= candidates[i]
        self.helper(candidates, i+1, curList, curSum, target, validSumList)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sort the candidates list to get duplicates side by side
        candidates.sort()

        validSumList = []
        curList = []
        self.helper(candidates, 0, curList, 0, target, validSumList)
        return validSumList