class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #O(N) time, ON Space solution
        #use set, add if not there, remvoe if already there, remaing number in set is signle
        s = set()
        for n in nums:
            if n in s:
               s.remove(n)
            else:
               s.add(n)

        return list(s)[0]