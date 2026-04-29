class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenBefore = {}
        for num in nums:
            if num in seenBefore:
                return True
            seenBefore[num] = num
        return False

         