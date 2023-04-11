class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        self.memo = {}
        return self.isMatchHelper(s, p)
    
    def isMatchHelper(self, s, p):
        if (s, p) in self.memo:
            return self.memo[(s,p)]
        if len(p) == 0 and len(s) == 0:
            return True
        elif len(p) == 0:
            return False
        elif len(s) == 0:
            return len(p) > 1 and len(p) % 2 == 0 and all(p[i] == "*" for i in range(1, len(p), 2))
        result = False
        if len(p) > 1 and p[1] == "*":
            if len(s) > 0 and s[0] == p[0] or p[0] == '.':
                result =  (
                    self.isMatchHelper(s[1:], p) # do the match without consuming the *, e.g. "aab", "a*b"
                    or self.isMatchHelper(s[1:], p[2:]) # do the match and consume the *, e.g. "ab", "a*b"
                    or self.isMatchHelper(s, p[2:]) # don't do the match, e.g. "a", "a*a"
                )
            else:
                result = self.isMatchHelper(s, p[2:]) # don't do the match, e.g. "a", "a*a"
        elif s[0] == p[0] or p[0] == '.':
            result = self.isMatchHelper(s[1:], p[1:])
        self.memo[(s,p)] = result
        return result
        

# test cases:
# "aa"
# "a"
# "aa"
# "a*"
# "ab"
# ".*"
# "aa"
# "aaa"
# "aabb"
# "a.*b"
# "abcdefghijklmnopqrst"
# "abcdefghijklmnopqrst"
# "aab"
# "c*a*b"
# "a"
# "ab*"
