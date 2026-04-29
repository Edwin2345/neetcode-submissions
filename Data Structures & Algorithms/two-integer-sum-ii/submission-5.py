class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers)-1

        while(L < R):
           numSum = numbers[L] + numbers[R]
           if numSum == target:
              return [L+1, R+1]
           elif numSum < target:
               L += 1
           else:
               R -= 1
        
        return [-1,-1]