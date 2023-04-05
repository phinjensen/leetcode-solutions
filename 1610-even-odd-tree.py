# BFS solution. Ugly!
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if root.val % 2 == 0:
            return False
        queue = collections.deque([root])
        depth = 0

        while queue:
            depth += 1
            mod = (depth + 1) % 2
            next_queue = collections.deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    if self.isValidNode(node.left.val, mod, next_queue):
                        next_queue.append(node.left)
                    else:
                        return False
                if node.right:
                    if self.isValidNode(node.right.val, mod, next_queue):
                        next_queue.append(node.right)
                    else:
                        return False
            
            queue = next_queue
        
        return True
    
    def isValidNode(self, val, mod, row):
        return val % 2 == mod and (
            len(row) == 0 or (
                mod and row[-1].val < val
            ) or (
                not mod and row[-1].val > val
            )
        )
