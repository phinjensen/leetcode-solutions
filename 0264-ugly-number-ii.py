# O(n) time (and space, I think).
# 
# A lot harder than it looked!

from collections import deque

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 5:
            return n
        start = (3, 4, 5)
        l = {
            2: deque(v * 2 for v in start),
            3: deque(v * 3 for v in start),
            5: deque(v * 5 for v in start),
        }
        u = 5
        while u < n:
            mini = min(l[i][0] for i in (2, 3, 5))
            for i in (2, 3, 5):
                if l[i][0] == mini:
                    l[i].popleft()
                l[i].append(mini * i)
            u += 1
        return l[2][-1] // 2
