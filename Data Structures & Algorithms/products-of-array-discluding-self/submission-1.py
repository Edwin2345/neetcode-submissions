class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #prefix, post fix
        # [.. 6 .] -> res[i] = prefix[i-1]* postfix[i+1]
        # [6...] -> res[i] = postfix[i+1]
        # [...6] -> res[i] = prefix[i-1]
        l = len(nums) 
        prefix = [nums[0]]*l
        postfix = [nums[l-1]]*l

        for i in range(1,l):
            prefix[i] = prefix[i-1]*nums[i]
        
        for i in range(l-2,-1,-1):
            postfix[i] = postfix[i+1]*nums[i]
        
        res = [postfix[1]]*l
        for i in range(1,l-1):
            res[i] = prefix[i-1]*postfix[i+1]
        res[l-1] = prefix[l-2] 

        return res