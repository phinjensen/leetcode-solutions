class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        expected = None
        while l < r:
            i = len(nums) // 2
            if list[i] == target:
                return i
            elif list[i] < target:
                # if the value at i is less than the target, then our left point
                # is now i, and we'd expect our next value at i to be *greater*
                expected = "greater"
                l = i
            elif list[i] > target:
                # in the opposite case, we move r, and we'd expect the new value
                # at i to be *less*
                expected = "less"
                r = i

        # If we never find an unexpected number (one which is greater when it should be less, or vice versa),
        # Then we know we've found the pivot, kinda. In the example below, the first iteration would find 1,
        # so it would move the right side to be 1 (index 3) and check 7 (index 1) next. The 7 is unexpected,
        # so we can move the left pointer to be pointing at it. We know now that everything to the right of
        # r and left of l is greater than our target.
        #
        # [6, 7, 0, 1, 2, 4, 5], target = 0
        # 
        # We can continue our binary search. If our new middle point is less than our target, we can just set
        # that point as our left point and continue. Like if our search portion looked like this:
        #
        # [7, -2, -1, 0, 1], target = 0
        # 
        # However, if it looked like this:
        #
        # [7, 8, 9, 0, 1], target = 0
        #
        # Then we'd find a 9 when we should expect something less than 1.
        #
        # Aha! I think that's the key! We just need to make sure that our value at l is less than the value at r
        # If it's not, then we need to move l to be at that value, or do the opposite if v[r] is lower than v[l]
