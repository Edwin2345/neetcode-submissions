class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
           if(hashMap.get((target-nums[i]), None) != None):
              ind = hashMap.get(target-nums[i])
              if(ind < i):
                 return [ind, i]
              else:
                 return [i, ind]
           hashMap[nums[i]] = i