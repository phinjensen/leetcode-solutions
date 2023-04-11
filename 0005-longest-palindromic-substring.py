class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        for i in range(len(s)):
            l, r = self.longestAtPosition(s, i, i+1)
            if r - l > len(best):
                best = s[l:r]
            l, r = self.longestAtPosition(s, i, i)
            if r - l > len(best):
                best = s[l:r]
        return best
    
    def longestAtPosition(self, s, l, r):
        while l >= 0 and r <= len(s):
            if s[l] == s[r-1]:
                l -= 1
                r += 1
            else:
                break
        l += 1
        r -= 1
        return (l, r)
