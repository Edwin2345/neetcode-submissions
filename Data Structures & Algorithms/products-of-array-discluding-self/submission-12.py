class Solution:
    # at least 2 num, so no abigious 1 or 0 elemtn cases
    # no division allowed
    # Optimizaiton from brute force: notice that we recompute the porduct form scratch ech tim
    # POAES = left side product * right side prouct, user a rolloing purdct arryas (prefix, suffix)
    #O(N) TC, O(1) extra space
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # calculate rolling products O(N) TC, O(N) SC
        leftSideProduct = [1] * len(nums)
        for i in range(1, len(nums)):
            leftSideProduct[i] = leftSideProduct[i - 1] * nums[i - 1]

        rightSideProduct = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            rightSideProduct[i] = rightSideProduct[i + 1] * nums[i + 1]

        # POAES = LSP * RSP O(N) TC, O(1) extrat sapce
        products = [0] * len(nums)
        for i in range(len(nums)):
            products[i] = leftSideProduct[i] * rightSideProduct[i]

        return products
