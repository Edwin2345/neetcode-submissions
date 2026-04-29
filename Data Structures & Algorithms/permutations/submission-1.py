class Solution:
    def helper(self, numSet, curPerm, allPerms):
        #reached the end of numSet -> add finished perm
        if len(numSet) == 0:
            allPerms.append(list(curPerm))
            return
        
        copySet = set(numSet)
        for el in copySet:
            #include current element from perm
            curPerm.append(el)
            numSet.remove(el)
            self.helper(numSet, curPerm, allPerms)
            #backtrack to remove element from perm
            curPerm.pop()
            numSet.add(el)

            


    def permute(self, nums: List[int]) -> List[List[int]]:
        #can solve it like subsets, but need to remove element from set every time
        allPerms = []
        curPerm = []
        numSet = set(nums)
        self.helper(numSet, curPerm, allPerms)
        return allPerms