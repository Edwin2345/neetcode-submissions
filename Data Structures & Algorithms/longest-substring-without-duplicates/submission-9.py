class Solution:
    #P: Sliding window + set, grow window while no duplicates
    #P: If duplicate, pop from left pointer until can insert
    #P: Calc distance for both cases, keep a max vairable
    # Time Compelxity: O(s) -> iterate throguh string
    # Space Complexity: O(s) -> at most store the entire string legnt
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        wordSet = set()
        L = 0
        for R in range(len(s)):             
            #shift window from left until we can add s[R]
            while L < len(s) and s[R] in wordSet:
                wordSet.remove( s[L] )
                L += 1

            #add new char to window and calc length
            wordSet.add( s[R] )
            maxLength = max(maxLength, R-L+1)         

        return maxLength