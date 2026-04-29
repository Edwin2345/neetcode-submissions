class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Naive division -> kinda hard
        tp = 1
        zeroCnt = 0 
        for n in nums:            
            if n == 0: zeroCnt += 1
            else: tp = tp*n

        if zeroCnt > 1:
            return [0]*len(nums)
        
        res = []
        for i in range(len(nums)):
            if zeroCnt == 1 and nums[i] == 0:
                res.append(tp)
            elif zeroCnt == 1:
                res.append(0)               
            else:
                res.append(int(tp/nums[i]))
        return res