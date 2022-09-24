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
// O(n) time complexity, O(log n) space complexity. VERY similar to 104, binary tree depth; in fact, my initial solution just used my solution for that and then did a stack-based scan. A bit ugly.
// This instead just keeps track of a max and compares the max of left and right branches as it goes up the tree.
var diameterOfBinaryTree = function(root) {
    let max = 0;

    var maxDepth = function (root) {
      if (root == null) {
        return 0;
      } else {
        let ld = maxDepth(root.left);
        let rd = maxDepth(root.right);
        max = Math.max(max, ld+rd);
        return 1+Math.max(ld, rd);
      }
    };
    maxDepth(root);
    return max;
};
