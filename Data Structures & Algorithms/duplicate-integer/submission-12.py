class Solution:
    #O(n), O(n) use a set -> check if already in set
    #O(n^2), O(1) -> 2 for loops to compare every single element
    #O(nlogn), O(1) -> sort, duplicates are side by side
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
           return False

        nums.sort()
        L=0
        for R in range(1,len(nums)):
            if nums[L] == nums[R]:
               return True
            L += 1
        return False   
