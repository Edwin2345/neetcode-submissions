class Solution:
    def findMin(self, nums: List[int]) -> int:
        #[5,4,1,2,3]
        # if mid is in right sorted half, search at least there
        # els ein left sorted have -> go to right

        L = 0
        R = len(nums)-1
        minVal = nums[0]

        while L <= R:
              mid = L + (R-L)//2
              #mid in right sorted portion -> update minVal and keep trying to go left
              if nums[mid] <= nums[R]:
                 minVal = min(minVal, nums[mid])
                 R = mid-1   
              #if in left sorted portion, go to the right one                 
              else:
                 L = mid+1
        
        return minVal