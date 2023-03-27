# O(n). This is the Dutch National Flag problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
# 
# The key intuition, taken from Wikipedia:
#
# > Entries from 0 up to (but not including) i are values less than mid,
# > entries from i up to (but not including) j are values equal to mid,
# > entries from j up to (and including) k are values not yet sorted, and
# > entries from k + 1 to the end of the array are values greater than mid.

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        k = len(nums) - 1
        while j <= k:
            if nums[j] < 1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
                j += 1
            elif nums[j] > 1:
                nums[j], nums[k] = nums[k], nums[j]
                k -= 1
            else:
                j += 1
