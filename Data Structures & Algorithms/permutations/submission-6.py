class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPerms = []

        def dfs(curPerm, usedIndices):
            #completed the permutation
            if len(usedIndices) == len(nums):
               allPerms.append( list(curPerm) )
               return

            #iterate through all indicies
            for i in range(len(nums)):
                #add i if not already used
                if i not in usedIndices:
                   curPerm.append( nums[i] )
                   usedIndices.add( i )

                   dfs(curPerm, usedIndices)

                   #pop and backtrack once done using, as we us same list refernce for curPerm
                   usedIndices.remove( i )
                   curPerm.pop() 
        
        dfs([], set())
        return allPerms