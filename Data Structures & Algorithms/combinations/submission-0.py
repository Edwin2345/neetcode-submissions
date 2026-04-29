class Solution:
    def getAllCombos(self, i, n, k, curCombo, allCombos):
        #found a valid combo of size k
        if len(curCombo) == k:
            allCombos.append(list(curCombo))
            return
        #reached end of range [1,n]
        if i > n:
            return
        
        #include current element in combo
        curCombo.append(i)
        self.getAllCombos(i+1, n, k, curCombo, allCombos)

        #backtrack and skip current element for combo
        curCombo.pop()
        self.getAllCombos(i+1, n, k, curCombo, allCombos)

    def combine(self, n: int, k: int) -> List[List[int]]:
        #combinations are just subsets of fixed size k
        allCombos = []
        curCombo = []
        self.getAllCombos(1, n, k, curCombo, allCombos)
        return allCombos 