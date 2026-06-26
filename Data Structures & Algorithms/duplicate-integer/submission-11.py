class Solution:
    #use a set -> check if already in set
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenBefore = set()
        for n in nums:
            if n in seenBefore:
               return True   
            seenBefore.add(n)
        return False