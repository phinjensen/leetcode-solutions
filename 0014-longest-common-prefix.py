class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = True
        out = []
        i = 0
        min_length = min(len(s) for s in strs)
        while i < min_length and common:
            common = True
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    common = False
                    break
            if common:
                out.append(c)
                i += 1
            else:
                break
        return "".join(out)
