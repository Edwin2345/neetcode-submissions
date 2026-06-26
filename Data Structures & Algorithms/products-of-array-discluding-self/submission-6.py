class Solution:
    #Q pass in empty list? -> no at least 2
    #P first try will use divsion, need extra attention to cases with zero
    #P if there is only ONE zero -> all non zero terms have a product of zero, zero will have non zero product
    #P if there is more than 1 zero -> entire array is just zeros
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #extra check just in case
        if len(nums) <= 1:
           return []

        zeroCount = 0
        newArr = [0]*len(nums)

        #find product, skip zero terms
        totalProd = 1
        for i in range(len(nums)):
            if nums[i] == 0:
               zeroCount += 1
            else:
               totalProd *= nums[i]
        
        #more than 1 zero -> products are all 0
        if zeroCount > 1:
           return newArr
        #exactly 1 zero -> the zero item is the only non zero product
        elif zeroCount == 1:
           for i in range(len(nums)):
               if nums[i] == 0:
                  newArr[i] = totalProd
        #no zeros, divide like normal
        else: 
            for i in range(len(nums)):
                newArr[i] = int(totalProd/nums[i])

        return newArr
