class Solution:
    def helper(self, numSet, curPerm, allPerms):
        #reached end of nums -> append copy of curPerm
        if len(numSet) == 0:
            allPerms.append(list(curPerm))
        
        #for current position, take all possible options
        copySet = set(numSet)
        for el in copySet:
            curPerm.append(el)
            numSet.remove(el)
            self.helper(numSet, curPerm, allPerms)
            #backtrack and try next element
            curPerm.pop()
            numSet.add(el)

    def permute(self, nums: List[int]) -> List[List[int]]:
        allPerms = []
        curPerm = []
        numSet = set(nums)
        self.helper(numSet, curPerm, allPerms)
        return allPerms