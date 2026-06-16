class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        newArr = [0]*(len(nums)*2)

        for i,n in enumerate(nums):
            newArr[i] = n
            newArr[i+len(nums)] = n
        
        return newArr