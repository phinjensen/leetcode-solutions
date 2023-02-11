class Solution:
    def isSqrt(self, n):
        return n == math.isqrt(n) ** 2

    def numSquares(self, n: int) -> int:
        if self.isSqrt(n):
            return 1
        squares = [1]
        best = [0, 1]
        for i in range(2, n+1):
            if self.isSqrt(i):
                squares.append(i)
                best.append(1)
            else:
                best.append(1 + min(best[i - square] for square in squares))
        return best[-1]
