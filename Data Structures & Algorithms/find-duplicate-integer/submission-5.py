class Solution:
    #O(N) time, O(1) space
    def findDuplicate(self, nums: List[int]) -> int:
        #find vaue where cycle begins
        slowPtr, fastPtr = 0, 0
        while True:
            slowPtr = nums[slowPtr]
            fastPtr = nums[nums[fastPtr]]
            if slowPtr == fastPtr:
               break

        #send off another slowptr from nums start
        #point where slow ptrs meet is duplciat e num,ber
        slowPtr2 = 0
        while True:
            slowPtr = nums[slowPtr]
            slowPtr2 = nums[slowPtr2]
            if slowPtr == slowPtr2:
               return slowPtr 