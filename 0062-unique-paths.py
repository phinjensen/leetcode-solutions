# O(n) because of memoization. I think this could be a lot simpler and more memory efficient if it just built up numbers on the fly going from the end back.
# Could have O(1) memory usage, I think.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}
        self.m = m
        self.n = n
        return self.helper(0,0)

    def helper(self, r, c):
        if r == self.m-1 or c == self.n-1:
            return 1
        if (r, c) in self.memo:
            return self.memo[(r,c)]
        result = 0
        if r + 1 < self.m:
            result += self.helper(r+1,c)
        if c + 1 < self.n:
            result += self.helper(r,c+1)
        self.memo[(r,c)] = result
        return result
