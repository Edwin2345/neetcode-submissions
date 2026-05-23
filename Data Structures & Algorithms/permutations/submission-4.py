class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        curPerm = []
        indicesUsed = set()

        def findPerms():
            #check if finished permutation
            if len(curPerm) == len(nums):
               perms.append( list(curPerm) )
               return
    
            #iterate through all indices
            for i in range(len(nums)):
                if i not in indicesUsed:
                    #add current eleemnt
                    curPerm.append(nums[i])
                    indicesUsed.add(i)

                    findPerms()
                    
                    #backtrack
                    curPerm.pop()
                    indicesUsed.remove(i)

        findPerms()
        return perms