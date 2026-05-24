class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        comboSums = []
        curCombo = []

        #sort so that duplciates are side by side
        candidates.sort()

        def findCombos(index, curSum):
            #found valid combo
            if curSum == target:
               comboSums.append( list(curCombo) ) 
               return            
            #edge case: index oob or blown past sum
            if index >= len(candidates) or curSum > target:
               return 

            #take current index 
            curCombo.append( candidates[index] )
            curSum += candidates[index]

            findCombos(index+1, curSum)

            #backtrack, skip all duplciates of this element           
            curVal = curCombo.pop()
            curSum -= candidates[index]  

            while index < len(candidates) and candidates[index] == curVal:
                index += 1

            findCombos(index, curSum)

        #call func
        findCombos(0,0)
        return comboSums