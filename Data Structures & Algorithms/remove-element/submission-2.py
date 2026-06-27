class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums) -1
        i = 0
        k = 0

        while i <= n:
            if nums[i] == val:
                k+=1
                nums[i], nums[n] = nums[n], nums[i]
                n-=1
            
            else:
                i += 1
        
        return len(nums) - k
