class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        #sort to get duplciates side by side
        candidates.sort()
        comboSums = []

        def genAllSums(curArr, i, sm):
            #found a valid combo sum
            if sm == target:
               comboSums.append(list(curArr))
               return
            #iterated throguh all candidates or already over target
            if i >= len(candidates) or sm > target:
               return
            
            #add current elemnt, and got to next
            curArr.append(candidates[i])
            sm += candidates[i]
            genAllSums(curArr, i+1, sm)

            #backtrack, skip this element, and all its duplicates
            curArr.pop()
            sm -= candidates[i]
            i += 1
            while i < len(candidates) and candidates[i] == candidates[i-1]:
                  i += 1
            genAllSums(curArr, i, sm)

        genAllSums([],0,0)
        return comboSums