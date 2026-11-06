class Solution:
    #rotated sorted, gives two
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]
        for n in nums:
            minNum = min(minNum, n)
        return minNum
        