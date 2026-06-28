class Solution:
    #POASS(i) = prefix[i]*syuffix[i]
    #nums = [a,b,c] prefix = [1,a,a*b] suffix = [b*c,c,1]
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        productList = [0]*len(nums)
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1]*nums[i+1]
        
        for i in range(len(nums)):
            productList[i] = prefix[i]*suffix[i]

        return productList