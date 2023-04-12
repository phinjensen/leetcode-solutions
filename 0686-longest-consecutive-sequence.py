# This is pretty much exactly the same as the official leetcode solution.
# I had a hard time getting the intuition. Here's what finally helped for me 
# to realize: If you can index numbers in O(1) time, it's just a matter of
# finding the starting points, which can be done by just checking if a number
# minus one is in the set. Once a starting point is found, just increment up
# from it until a number isn't in the set.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        num_set = set(nums)
        for num in num_set:
            if num - 1 not in num_set:
                streak = 1
                current = num

                while current + 1 in num_set:
                    current += 1
                    streak += 1
                
                best = max(best, streak)
        return best
