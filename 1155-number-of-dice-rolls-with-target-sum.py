# Top-down solution. Worked most of it out in mock interview. Lesson learned: Don't assume the result of dict.get will be boolean truthy if the value exists.
class Solution:
    _mod = 10**9 + 7
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.memo = {}
        return self.possible_rolls(n, k, target)
    
    def possible_rolls(self, r: int, k: int, target: int) -> int:
        if self.memo.get((r,target)) != None:
            return self.memo[(r,target)]

        if r == 0 or target < 0:
            return 0
        elif r == 1:
            if target > 0 and target <= k:
                return 1
            else:
                return 0

        result = 0
        for face in range(1, k+1):
            result += self.possible_rolls(r - 1, k, target - face)
        self.memo[(r,target)] = result
        return result % self._mod

# Bottom-up solution. Conceptually harder, but a much simpler implementation
class Solution:
    _mod = 10**9 + 7
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # Rows are rolls, columns are target
        memo = [
            [0 for i in range(target)],
            [1 if i < k else 0 for i in range(target)],
        ]
        for r in range(2, n+1):
            memo.append([])
            for t in range(target):
                memo[-1].append(sum(memo[-2][max(0,t-k):max(0,t)]))
        return memo[-1][-1] % self._mod
