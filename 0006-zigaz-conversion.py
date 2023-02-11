# Solution 1
#class Solution:
#    def convert(self, s: str, num_rows: int) -> str:
#        if num_rows == 1:
#            return s
#        block_width = max(1, num_rows - 1)
#        num_columns = block_width * (len(s) // num_rows) + 1
#        mat = [[None for j in range(num_columns)] for i in range(num_rows)]
#
#        up = False
#        r, c = 0, 0
#        for char in s:
#            mat[r][c] = char
#            if up:
#                r -= 1
#                c += 1
#                if r == 0:
#                    up = False
#            else:
#                r += 1
#                if r == num_rows - 1:
#                    up = True
#
#        result = []
#        for r in range(num_rows):
#            for c in range(num_columns):
#                if mat[r][c]:
#                    result.append(mat[r][c])
#
#        return "".join(result)
class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s
        result = []
        start = 0
        c = 0
        long = not (num_rows % 2)
        while len(result) < len(s):
            result.append(s[c])
            if start != 0 and start != num_rows - 1:
                if long:
                    step = (num_rows - c) * 2
                else:
                    step = c * 2
            else:
                step = (num_rows - 1) * 2
            long = not long
            c += step
            if c >= len(s):
                c = start + 1
                start = c
        return "".join(result)


s = Solution()
print(s.convert("PAYPALISHIRING", 3))
print(s.convert("PAYPALISHIRING", 4))
print(s.convert("A", 1))
print(s.convert("AB", 1))
