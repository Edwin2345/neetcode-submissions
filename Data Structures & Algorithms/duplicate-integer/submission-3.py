class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenBefore = set()
        for num in nums:
            if num in seenBefore:
                return True
            seenBefore.add(num)
        return False

         