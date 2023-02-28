class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i, row in enumerate(triangle[1:], start=1):
            for j in range(len(row)):
                prev = triangle[i-1]
                if j == 0:
                    row[j] += prev[0]
                elif j == len(row) - 1:
                    row[j] += prev[-1]
                else:
                    row[j] += min(prev[j-1], prev[j])
        return min(triangle[-1])
