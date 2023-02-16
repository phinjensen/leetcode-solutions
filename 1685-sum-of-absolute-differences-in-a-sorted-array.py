class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        suffix_total = sum(nums)
        prefix_total = 0
        for i, num in enumerate(nums):
            suffix_total -= num
            nums[i] = abs(prefix_total - i * num) + suffix_total - (len(nums) - 1 - i) * num
            prefix_total += num
        return nums
