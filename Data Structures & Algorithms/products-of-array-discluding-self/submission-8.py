class Solution:
    #N: at least 2 elements
    #P: >1 zero then entire num array is zero's
    #P: extacly 1 zero ->  0 element is non zeor, rest isnt
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0
        totalProduct = 1
        productList = [0]*len(nums)
        for n in nums:
            if n == 0:
               zeroCount += 1
            else:
               totalProduct *= n

        if zeroCount == 1:
           for i in range(len(nums)):
                if nums[i] == 0:
                   productList[i] = totalProduct 
        elif zeroCount == 0:
            for i in range(len(nums)):
                productList[i] = totalProduct // nums[i]
        
        return productList
        