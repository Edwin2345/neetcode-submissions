class Solution:
    # if (R-L+1) - max(freqMap) <= k, we can grow
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        freqMap = defaultdict(int)

        L = 0
        for R,ch in enumerate(s):
            #add current element
            freqMap[ch] += 1

            #shrink window until we have valid replacement string
            while (R-L+1) - max(freqMap.values()) > k:
                freqMap[s[L]] -= 1
                L += 1
            
            #mesure and update max lenght
            maxLength = max(maxLength, R-L+1)
        
        return maxLength
        