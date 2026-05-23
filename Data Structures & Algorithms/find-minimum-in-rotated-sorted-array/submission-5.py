class Solution:
    def findMin(self, nums: List[int]) -> int:
        minVal = nums[0]
        L = 0
        R = len(nums) - 1

        while L <= R:
          mid = L + (R-L)//2

          #in right sorted half -> correct side but kepe on shrinking window
          if nums[mid] <= nums[R]:
             minVal = min(nums[mid], minVal)
             R = mid - 1
          #left sorted half, go to gith
          else:
             L = mid + 1
        
        return minVal

                