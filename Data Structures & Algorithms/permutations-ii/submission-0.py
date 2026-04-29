class Solution:
    def helper(self, nums, curPerm, allPerms):
        #finished perm
        if len(nums) == 0:
            allPerms.append(list(curPerm))
            return
        
        #for cur position, insert every unique element
        used = set()
        numLength = len(nums)
        for i in range(numLength):
            #already used in iteration (duplicate value)
            el =  nums[i]
            if el in used:
                continue

            #insert first element
            curPerm.append(el)
            used.add(el)
            nums.pop(i)
            self.helper(nums,curPerm,allPerms)

            #backtrack, remove elemtn and insert back at end of nums
            curPerm.pop()
            nums.insert(i,el)
        
        return allPerms

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:        
        return self.helper(nums,[],[])