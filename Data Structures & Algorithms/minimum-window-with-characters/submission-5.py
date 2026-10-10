class Solution:
    # substring --> contrinous string right?
    # does not have to be in oprder - freq have to match
    # idea: grow substring from  right until match
    # once we have a match, start poping form the lef tot mimize --> if still match save substring
    def minWindow(self, s: str, t: str) -> str:
        # edge case: if s is shorter than t no possible match
        if len(s) < len(t):
            return ""

        # build freq map of characters in t
        tFreq = defaultdict(int)
        for ch in t:
            tFreq[ch] += 1

        # slide windows through s
        matches, minSS = 0, ""
        sFreq = defaultdict(int)
        L = 0
        for R in range(len(s)):
            # add the current character to SS and see if match form
            sFreq[s[R]] += 1
            if s[R] in tFreq and sFreq[s[R]] == tFreq[s[R]]:
                matches += 1

            # check if found a valid window, update min and try to shrink from left
            while matches == len(tFreq):
                if minSS == "" or R - L + 1 < len(minSS):
                    minSS = s[L : R + 1]

                sFreq[s[L]] -= 1
                if s[L] in tFreq and sFreq[s[L]] < tFreq[s[L]]:
                    matches -= 1
                L += 1

        return minSS
