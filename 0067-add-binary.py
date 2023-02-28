# O(n) time and space
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a)-1, len(b)-1
        carry = 0
        while i >= 0 or j >= 0:
            _sum = carry
            if i >= 0:
                _sum += int(a[i])
                i -= 1
            if j >= 0:
                _sum += int(b[j])
                j -= 1
            result.append(_sum % 2)
            carry = _sum // 2
        
        if carry:
            result.append(carry)
        
        return "".join(str(c) for c in reversed(result))
