# My initial solution, which I believe is something like O(2^n) but much faster than that in reality.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.results = set()
        self.helper(target, [])
        return list(self.results)
    
    def helper(self, target: int, progress: List[int]):
        if target == 0:
            return sorted(progress)
        if target < 0:
            return None
        for candidate in self.candidates:
            result = self.helper(target - candidate, [*progress, candidate])
            if result:
                self.results.add(tuple(result))

# The problem of unique items and dealing with sorting can be handled by only checking candidates
# that are equal to or larger than the last one checked, which maintains sorting and uniqueness
# automatically. This runs *much* faster in reality. About 10x speed.

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.candidates = candidates
        self.results = []
        self.helper(target, ())
        return self.results
    
    def helper(self, target: int, progress: List[int]):
        if target == 0:
            return progress
        if target < 0:
            return None
        for candidate in self.candidates:
            if not progress or candidate >= progress[-1]:
                result = self.helper(target - candidate, [*progress, candidate])
                if result:
                    self.results.append(result)
