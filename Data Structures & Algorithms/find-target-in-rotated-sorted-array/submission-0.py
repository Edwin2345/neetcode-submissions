class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Rotate -> shift first to end
        [0,1,2,3,4,5]
        [1,2,3,4,5,0]
        [2,3,4,5,0,1]

         *NOTICE -> you have 2 sorted portions (in increasing order)
                 -> one portion will have all numebrs striclty less than other
                 -> find which sorted persion in, then do normal binary search

         -> if < is in right sorted portion  M < L
         
         4,5, |  0,1,2,3
         L       M     R

             --> if target > R --> search LSP instead -> R = M-1
             --> if M < target --> search RSP -> L = M + 1
             --> if target < M --> search RSP -> R = M-1

         -> if M is in left sorted portion, M >= L

         2,3,4,5  | 0,1         
         L     M      R      

             --> if target < L <= M --> search RSP instead -> L = M+1
             --> if L <= target < M --> search LSP R = M-1
             --> if L <= M < target --> search LSP L = M+1
                
        '''

        L=0
        R=len(nums)-1
        while(L <= R):
            M = L + (R-L)//2
            if nums[M] == target:
                return M
            #mid in right sorted portion
            if nums[M] < nums[L]:
                if target > nums[R] or target < nums[M]:
                    R = M-1
                else:
                    L = M+1
            #mid in left sorted portion
            else:
                if target < nums[L] or nums[M] < target:
                  L = M+1
                else:
                  R = M-1
        return -1