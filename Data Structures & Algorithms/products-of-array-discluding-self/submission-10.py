class Solution:
    # [1,2,3,4]  [24, 12, 8, 6]
    # empty list? list with one element --> NO
    # idea, POAES, mean multiply all numbers before, and all numbers after
    # all numbers before is prefix area, all after is suffice array
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputList = [0]*len(nums)

        #build prefix and suffix array 
        prefix, prod = [0]*len(nums), 1
        for i in range(len(nums)):
            prod *= nums[i]
            prefix[i] = prod 

        suffix, prod = [0]*len(nums), 1
        for i in range(len(nums)-1,-1,-1):
            prod *= nums[i]
            suffix[i] = prod
        
        #build output
        for i in range(len(nums)):
            leftProd = prefix[i-1] if i-1 >= 0 else 1
            rightProd = suffix[i+1] if i+1 < len(nums) else 1
            outputList[i] = leftProd * rightProd

        return outputList
        