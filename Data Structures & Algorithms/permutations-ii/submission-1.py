class Solution:
    def helper(self, nums, curPerm, allPerms):
        #finished perm
        if len(nums) == 0:
            allPerms.append(list(curPerm))
            return
        
        #for cur position, insert every unique element
        used = set()
        for i in range(len(nums)):
            #already used in iteration (duplicate value)
            el =  nums[i]
            if el in used:
                continue

            #insert ith elemen at this spot
            curPerm.append(el)
            used.add(el)
            nums.pop(i)
            self.helper(nums,curPerm,allPerms)

            #backtrack, remove element from perm and add back to nums
            curPerm.pop()
            nums.insert(i,el)
        
        return allPerms

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:        
        return self.helper(nums,[],[])