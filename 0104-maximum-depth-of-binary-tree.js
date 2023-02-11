/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */

// Recursive solution, O(n), n is the number of nodes. Space complexity is O(m) where m is that max depth of the tree. I believe that's the same as O(log n).
var maxDepth = function (root) {
  if (root == null) {
    return 0;
  } else {
    return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
  }
};
