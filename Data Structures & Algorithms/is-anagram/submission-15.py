class Solution:
    # only lowercase letters,anagram = same freq but possibly diff order
    # O(nlogn) TC, O(1) SC --> sort the 2 strigns lexographically
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
           return False

        return "".join(sorted(s)) == "".join(sorted(t))
        