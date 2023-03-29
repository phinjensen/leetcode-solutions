# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node, val):
        if not node:
            return val
        val = val * 10 + node.val
        total = 0
        if not node.left and not node.right:
            return val
        if node.left:
            total += self.dfs(node.left, val)
        if node.right:
            total += self.dfs(node.right, val)
        return total
