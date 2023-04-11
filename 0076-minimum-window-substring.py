from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        r = 0
        t_counter = Counter(t)
        counter = Counter()
        best = (-math.inf,math.inf)
        while r < len(s):
            counter[s[r]] += 1
            if (t_counter - counter).total() == 0:
                while l < r and counter[s[l]] > t_counter[s[l]]:
                    counter[s[l]] -= 1
                    l += 1
                #print(l,r)
                if best[1] - best[0] > r - l:
                    best = (l, r)
            r += 1
        if best[0] == -math.inf:
            return ""
        else:
            return s[best[0]:best[1]+1]
