# Again, O(n) time complexity, but this time I think it has O(n) space complexity as well, which is a bit ugly.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.memo = {}
        self.nums = nums
        self.counts = dict((n, self.nums.count(n)) for n in self.nums)
        self.helper(())
        return self.result
    
    def helper(self, progress):
        if len(progress) == len(self.nums):
            self.result.append(progress)
        else:
            for n in self.nums:
                if progress.count(n) != self.counts[n] and (*progress, n) not in self.memo:
                    self.memo[(*progress, n)] = self.helper((*progress, n))
