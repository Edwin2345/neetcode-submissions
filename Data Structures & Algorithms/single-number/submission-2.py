class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #O(N) time, O(1) space solutn
        #XOR the same number will cancel out, anmd xor is communatikve
        n = nums[0]
        for i in range(1,len(nums)):
            n = n ^ nums[i]
        return n
            