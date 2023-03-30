# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if nums:
            max_i = max(range(len(nums)), key=lambda i: nums[i])
            return TreeNode(
                nums[max_i],
                self.constructMaximumBinaryTree(nums[:max_i]),
                self.constructMaximumBinaryTree(nums[max_i+1:]),
            )
        return None
