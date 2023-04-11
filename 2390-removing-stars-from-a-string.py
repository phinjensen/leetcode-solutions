class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == '*':
                stack.pop()
            else:
                stack.append(c)
            i += 1
        return "".join(stack)
