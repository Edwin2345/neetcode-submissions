class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        allPerms = []

        def generatePerms(curPerm, i, usedSet):
            # add current value
            curPerm.append(nums[i])
            usedSet.add(nums[i])

            #add final perm if complete, otherwise continue recursion
            if len(curPerm) == len(nums):
               allPerms.append(list(curPerm))
            else:
                for j in range(len(nums)):
                    if nums[j] not in usedSet:
                       generatePerms(curPerm, j, usedSet)       
            
            #backtrack and use a differnt value at this position
            curPerm.pop()
            usedSet.remove(nums[i])

        #run generate perms with all iniial posible staritng values
        for i in range(len(nums)):
            generatePerms([], i, set())

        return allPerms
        