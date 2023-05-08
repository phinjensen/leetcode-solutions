# A fun use of zip and range, but kinda ugly:
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        for (i1, j1), (i2, j2) in zip(
                zip(
                    range(len(mat)), range(len(mat))
                ),
                zip(
                    range(len(mat)),
                    reversed(range(len(mat)))
                )
            ):
            result += mat[i1][j1]
            if not (i1 == i2 and j1 == j2):
                print(i1, j1, i2, j2)
                result += mat[i2][j2]
        return result

# Probably more clear, if nothing else:
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        result = 0
        l = 0
        r = len(mat[0]) - 1
        for i, row in enumerate(mat):
            result += row[l]
            if l != r:
                result += row[r]
            l += 1
            r -= 1
        return result
