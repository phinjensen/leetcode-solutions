# O(n) solution, but kinda ugly. I can't really think of a better way to do it, to be honest. 
class Solution:
    def calculate(self, s: str) -> int:
        s = re.split(r"([*/+-])", s.replace(' ', ''))
        stack = []
        for chunk in s:
            if chunk.isnumeric():
                val = int(chunk)
                if stack and stack[-1] in '*/':
                    op = stack.pop()
                    result = stack.pop()
                    if op == '*':
                        result *= int(chunk)
                    elif op == '/':
                        result = int(result / int(chunk))
                    stack.append(result)
                else:
                    stack.append(val)
            else:
                stack.append(chunk)
        stack = stack[::-1]
        while len(stack) > 1:
            lhs = stack.pop()
            op = stack.pop()
            rhs = stack.pop()
            if op == '+':
                stack.append(lhs + rhs)
            elif op == '-':
                stack.append(lhs - rhs)
        return stack[-1]
