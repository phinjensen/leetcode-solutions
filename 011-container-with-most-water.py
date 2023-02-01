# O(n) time, O(1) space
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        best = (right - left) * min(height[left], height[right])
        while left < right:
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            capacity = (right - left) * min(height[left], height[right])
            best = max(capacity, best)
        return best
