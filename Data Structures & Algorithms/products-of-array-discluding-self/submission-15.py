class Solution:
    # at least 2 num, so no abigious 1 or 0 elemtn cases
    # no division allowed
    # Optimizaiton from brute force: notice that we recompute the porduct form scratch ech tim
    # POAES = left side product * right side prouct, usea rollign product
    #O(N) TC, O(1) SC
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [0] * len(nums)

        # apply leftSideProduct O(N) TC, O(1) SC
        leftSideProduct = 1
        for i in range(len(nums)):
            products[i] = leftSideProduct
            leftSideProduct *= nums[i]
        
        # apply rightSide product ontop of leftSideprouct  O(N) TC O(1) SC
        rightSideProduct = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= rightSideProduct
            rightSideProduct *= nums[i]

        return products
