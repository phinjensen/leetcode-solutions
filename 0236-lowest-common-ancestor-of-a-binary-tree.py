class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.found = False
        self.ancestors = []
        self.p = p
        self.q = q

        self.dfs(root)

        return self.ancestors[-1]

    def dfs(self, node):
        if not self.found:
            self.ancestors.append(node)
        if node == self.p or node == self.q:
            if self.found:
                return True
            else:
                self.found = True
        if node.left and self.dfs(node.left):
            return True
        if node.right and self.dfs(node.right):
            return True
        if self.ancestors[-1] == node:
            self.ancestors.pop()
