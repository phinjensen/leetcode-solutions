# My attempt. It is O(log n), but it's pretty clunky and I got things wrong due to edge cases a couple of times.
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 2
        last_seen = -1
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-2] != nums[-1]:
            return nums[-1]
        while l < r:
            m = (l + r) // 2
            if m % 2:
                m += 1
            if nums[m] != nums[m+1]:
                last_seen = nums[m]
                r = m - 2
            else:
                l = m
        return last_seen
