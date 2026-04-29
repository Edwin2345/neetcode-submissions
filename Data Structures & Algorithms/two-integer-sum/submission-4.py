class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHashMap = {}
        for i in range(len(nums)):
           if( (target-nums[i]) in prevHashMap):
              return [prevHashMap[target-nums[i]], i]
           prevHashMap[nums[i]] = i