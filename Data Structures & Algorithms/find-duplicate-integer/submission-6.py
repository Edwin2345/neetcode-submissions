class Solution:
    #there will be cycle as each num is in the rang of the indices but duplicate means 2 paths to same val
    #find where cycle starts, the send another slow ptr from start
    #where these 2 slow ptrs intersect is the duplicate as that is where
    def findDuplicate(self, nums: List[int]) -> int:
        slowPtr, fastPtr = 0, 0 
        while True:
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]
            if slowPtr == fastPtr:
               break

        slowPtr2 = 0
        while True:
            slowPtr2 = nums[slowPtr2]
            slowPtr = nums[slowPtr]
            if slowPtr2 == slowPtr:
               return slowPtr2   
        