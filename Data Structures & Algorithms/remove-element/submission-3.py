class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n = len(nums)
        end_val = n-1
        k = 0
        i = 0

        while i <= end_val:
            if nums[i] == val:
                k+=1
                nums[i], nums[end_val] = nums[end_val], nums[i]
                end_val -= 1
            
            else:
                i += 1
        
        return n - k
        