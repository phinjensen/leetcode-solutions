class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            c = t[j]
            if s[i] == c:
                i += 1
            j += 1
        if i == len(s):
            return True
        return False
