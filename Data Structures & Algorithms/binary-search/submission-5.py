class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searchRec( nums, target, low, high):
             if low > high:
                return -1
            
             mid = low + (high-low)//2
             if(nums[mid] == target):
                return mid
             elif(nums[mid] < target):
                return searchRec(nums, target, mid+1, high)
             else:
                return searchRec(nums, target, low, mid-1)
        
        return searchRec(nums, target, 0, len(nums)-1)

       

        