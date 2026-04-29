class Solution:
    def getAllCombos(self, i, n, k, curCombo, allCombos):
        #found a valid combo of size k
        if len(curCombo) == k:
            allCombos.append(list(curCombo))
            return
        #reached end of range [1,n]
        if i > n:
            return
        
        #OPTIMIZATION ->generate combos with 1st (1 to n), 2nd (x+1 to n) where x is what's 1st
        for j in range(i,n+1):
            curCombo.append(j)
            self.getAllCombos(j+1, n, k, curCombo, allCombos)
            curCombo.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        #OPTIMIZATION ->generate combos with 1st (1 to n), 2nd (x+1 to n) where x is what's 1st
        allCombos = []
        curCombo = []
        self.getAllCombos(1, n, k, curCombo, allCombos)
        return allCombos 