class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        for i in range(1, len(prefix)):
            prefix[i] = nums[i-1] * prefix[i-1]
        nums = nums[::-1]
        suffix = [1] * len(nums)
        for i in range(1, len(suffix)):
            suffix[i] = nums[i-1] * suffix[i-1]
        suffix = suffix[::-1]
        return [prefix[i] * suffix[i] for i in range(len(nums))]
