class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        expected = None
        while l < r:
            i = (l + r) // 2
            if nums[i] == target:
                return i
            if nums[l] > nums[r]:
                if nums[i] > target:
                    r = i
                elif nums[i] < target
                    l = i
            elif nums[i] < target:
                l = i
            elif nums[i] > target:
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
        # [7, 8, 9, -4, -3, -2, -1, 0, 2, 4, 5], target = 0
        #  l                                 r
        # The middle here is -2, which we know is less than 0. -2 is also less than v[r], so we can treat this normally.

        # [4,5,6,-1,0,1,2] target=5
        #  l            r
        # The middle here is 7, which is greather than 0, so we would normally set r to be at 7.
        # HOWEVER, because our value at l is GREATER than our target 0, we instead move l to be at 7.
        #
        # [4,5,6,7,0,1,2] target=3
        #  l           r
        # Them middle here is 7, which is greater than our target, so we would normally set r to be at 7.
        # Because v[r] < target < v[l], return -1
        #
        # [4,5,6,7,0,1,2] target=5
        #  l           r
        # 7 > 5, move r to be 7 because v[l] < target

        # possibilities:
        #     v[m] > target AND v[l] < target ->   normal (r->m)
        #     v[m] > target AND v[l] > target -> abnormal (l->m)
        #     v[m] < target AND v[r] < target -> abnormal (r->m)
        #     v[m] < target AND v[r] > target ->   normal (l->m)

        #
        # Then we'd find a 9 when we should expect something less than 1.
        #
        # Aha! I think that's the key! We just need to make sure that our value at l is less than the value at r
        # If it's not, then we need to move l to be at that value, or do the opposite if v[r] is lower than v[l]
