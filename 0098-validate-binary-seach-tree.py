# O(n) time, O(log n) space. Another case where I need to *be careful of treating variables as booleans*! A value can be 0 and still be something I want to compare against. If a node is 0, then the child node validity check might fail because it treats the gt or lt variable as False and skips that check. This could have been avoided with math.inf and -math.inf from the beginning.
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidNode(root, math.inf, -math.inf)
    
    def isValidNode(self, node: TreeNode, lt: int | float, gt: int | float) -> bool:
        if node.val >= lt or node.val <= gt:
            return False
        if node.left and not self.isValidNode(node.left, node.val, gt):
            return False
        if node.right and not self.isValidNode(node.right, lt, node.val):
            return False
        return True
