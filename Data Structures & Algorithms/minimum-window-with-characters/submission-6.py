class Solution:
    # find the min substring thats letetr freq matches t
    def minWindow(self, s: str, t: str) -> str:
        # edge case, t larger than s
        if len(t) > len(s):
            return ""

        # freq map t
        tFreq = defaultdict(int)
        for letter in t:
            tFreq[letter] += 1

        # slide window over s until it substrign found
        L, sFreq = 0, defaultdict(int)
        matches = 0
        minSS = ""
        for R in range(len(s)):
            # add R and update matches
            sFreq[s[R]] += 1
            if s[R] in tFreq and tFreq[s[R]] == sFreq[s[R]]:
                matches += 1            

            # valid substring found
            while matches == len(tFreq):
                # update min substring
                if minSS == "" or len(minSS) > R - L + 1:
                    minSS = s[L : R + 1]

                # try to shrink form left
                if s[L] in tFreq and tFreq[s[L]] == sFreq[s[L]]:
                    matches -= 1
                sFreq[s[L]] -= 1
                L += 1

        return minSS
