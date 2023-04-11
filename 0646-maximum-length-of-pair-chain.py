class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort( key=lambda x: x[1])
        a, b = pairs[0]
        result = 1
        i = 0
        while i < len(pairs):
            c, d = pairs[i]
            if b < c:
                a, b = c, d
                result += 1
            i += 1

        return result
