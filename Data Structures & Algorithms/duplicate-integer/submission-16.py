class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupMap = {}
        hasDup = False
        for i in range(len(nums)):
            if nums[i] in dupMap:
               hasDup = True
               dupMap[nums[i]].append(i) 
            else:
               dupMap[nums[i]] = [i] 
        
        #print a map of duplciates
        for k,v in dupMap.items():
            if len(v) > 1:
               print(str(k) + " occurs at indicies " + str(v))
        return hasDup

        