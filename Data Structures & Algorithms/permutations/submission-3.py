class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        numSet = set(nums)
        curPerm = []
        allPerms = []
        
        def dfs():
            #finished perm
            if len(numSet) == 0:
                allPerms.append(list(curPerm))
                return
            
            #make a copy over set your iterating due to python weirdness
            for n in numSet.copy():
                #perm that includes n in this position
                curPerm.append(n)
                numSet.remove(n)
                dfs()
                #backtrack to place next n value at this position
                curPerm.remove(n)
                numSet.add(n)

        dfs()
        return allPerms