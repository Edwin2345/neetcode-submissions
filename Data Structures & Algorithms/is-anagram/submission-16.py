class Solution:
    # only lowercase letters,anagram = same freq but possibly diff order
    # O(nlogn) TC, O(n) SC as makes copies of strings --> sort the 2 strigns lexographically
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False

        return "".join(sorted(s)) == "".join(sorted(t))
        