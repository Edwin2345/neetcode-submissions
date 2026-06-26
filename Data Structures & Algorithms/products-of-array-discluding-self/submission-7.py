class Solution:
    #P: we can can product except self if we know the products of the left side and right side
    #P: prodcut of left side is the prefix product, product of right side is suffix product
    #[2,3,4,5,6]
    #Prefix: [1,2,6,24,120]
    #Suffix: [360,120,30,6,1]
    #POAAS(nums[1]) = prefix[1]*suffix[1] = 2*120 = 240 
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        suffix = [1]*len(nums)
        productList = [0]*len(nums)

        #build prefix and suffix
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            suffix[i] = suffix[i+1]*nums[i+1]

        #calculate POAAS
        for i in range(len(nums)):
            productList[i] = prefix[i]*suffix[i]

        return productList
