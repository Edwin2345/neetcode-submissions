class Solution:
    #use two poitners at both ends (smallest and largest)
    #ad both,. if two large, shift R inwars to smaller, if too large shift L inwards
    #O(N) time and O(1) space
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L,R  = 0, len(numbers)-1

        while L < R:
            sm = numbers[L] + numbers[R]
            if sm  == target:
               return [L + 1, R + 1]
            elif sm < target:
               L += 1
            else:
               R -= 1

        #not found (tech not possible)
        return [-1, -1]  

        