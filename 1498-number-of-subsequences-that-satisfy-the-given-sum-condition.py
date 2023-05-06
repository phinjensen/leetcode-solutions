# Basically couldn't figure it out on my own. I think the intuition that I was missing was using a left pointer and considering it as static and anything to the right pointer as valid.
# Move the left pointer and repeat until it doesn't work, then move the right pointer until it does again.
MOD = 10**9 + 7
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = 0
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                result = (result + 2**(r - l)) % MOD
                l += 1
            else:
                r -= 1
        return result
