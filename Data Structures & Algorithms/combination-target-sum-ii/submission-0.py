class Solution:
    def helper(self, candidates, i, target, curCombo, allCombos):
        #found valid combo
        if target == 0:
           allCombos.append(list(curCombo))           
           return
        #reached end of candidates list
        if i >= len(candidates):
           return

        #create a combo including current value
        curCombo.append(candidates[i])
        self.helper(candidates, i+1, target-candidates[i], curCombo, allCombos)

        #backtrack and create a combo where duplicates aren't used
        curVal = curCombo.pop()
        while(i+1 < len(candidates) and candidates[i] == candidates[i+1]):
             i += 1
        self.helper(candidates, i+1, target, curCombo, allCombos)

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates or target == 0: 
            return []

        #subset approach but sum must equal target
        candidates.sort()
        allCombos = []
        curCombo = []
        self.helper(candidates, 0, target, curCombo, allCombos)
        return allCombos