# O(n!), I believe. I don't think it's possible to do better than that!
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        self.nums = nums
        self.helper([])
        return self.result
    
    def helper(self, progress):
        if len(progress) == len(self.nums):
            self.result.append(progress)
        else:
            for n in self.nums:
                if n not in progress:
                    self.helper(progress + [n])
