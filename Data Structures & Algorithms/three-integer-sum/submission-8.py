class Solution:
    # better solution, sort and use 3 pointers
    # fix one and run two sum II, if equal shift both to next unique pair
    # skip duplicates at every pointer
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i in range(len(nums)):
            # skip duplicate nums
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            # run two sum II on the remainign window
            L, R = i + 1, len(nums) - 1
            while L < R:
                sm = nums[L] + nums[R] + nums[i]
                # found match, save and shfit both to next unqiue
                if sm == 0:
                    triplets.append([nums[i], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    while L < R and nums[L] == nums[L - 1]:
                        L += 1
                    while L < R and nums[R] == nums[R + 1]:
                        R -= 1
                # sum too small
                elif sm < 0:
                    L += 1
                # sum too large
                else:
                    R -= 1

        return triplets
