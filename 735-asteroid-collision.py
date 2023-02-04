# O(n) time, but also O(n) space, because it's creating a second list.
# I don't know that it could be done in smaller space complexity, because
# any in-place removals would be O(n) time. Other data structures might
# do better, but that would require copying, which would be O(n)... unless
# fancy conversions are okay.
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        remaining = []

        i = 0
        while i < len(asteroids):
            asteroid = asteroids[i]
            if not remaining or asteroid > 0 or remaining[-1] < 0:
                remaining.append(asteroid)
            elif remaining[-1] <= abs(asteroid):
                if remaining.pop() < abs(asteroid):
                    continue
            i += 1
        
        return remaining
