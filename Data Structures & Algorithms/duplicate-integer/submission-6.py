class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenBefore = set()
        for i in nums:
            if i in seenBefore:
                return True
            seenBefore.add(i)
        return False