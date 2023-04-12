import re

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = re.sub(r'/+', '/', path)
        path = path.rstrip('/')
        dirs = path.split('/')
        result = []
        for d in dirs:
            if d == '..':
                if len(result) > 1:
                    result.pop()
            elif d != '.':
                result.append(d)
        return "/".join(result) or "/"
