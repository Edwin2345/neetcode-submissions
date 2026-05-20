class Solution:
    #assumption, can always fidn soltuion
    def jump(self, nums: List[int]) -> int:
        #greedy: BFS like
        # keep track of regions we can jump to givne the current node valu
        #then in next region, find the locally optium (max yindex you can jump)
        # and go to next region
           
        L,R = 0,0
        farthestIndex = 0
        numJumps = 0
        while R < len(nums)-1:
          #scan region to find largest jump (locally optimnum)
          for i in range(L,R+1):
              farthestIndex = max(farthestIndex,nums[i] + i)
          #go to new region (requires 1 jump)
          L = R+1
          R = farthestIndex
          numJumps += 1
        
        return numJumps
