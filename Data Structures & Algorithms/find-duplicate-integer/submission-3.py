class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # same as asking for head of cycle
        fast = 0
        slow = 0
        slow2 = 0
 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if(slow == fast):
                break

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if(slow == slow2):
                break

        return slow2