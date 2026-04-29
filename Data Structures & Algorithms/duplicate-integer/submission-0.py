class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenBefore = {}
        for el in nums:
            if el in seenBefore:
                return True
            else:
                seenBefore[el] = el
        return False
         