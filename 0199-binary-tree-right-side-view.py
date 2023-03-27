# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while len(queue) > 0:
            next_queue = collections.deque()
            result.append(queue[-1].val)
            while queue:
                node = queue.popleft()

                if node and node.left:
                    next_queue.append(node.left)
                if node and node.right:
                    next_queue.append(node.right)
            
            queue.extend(next_queue)
        return result
