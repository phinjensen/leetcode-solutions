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
 * @return {TreeNode}
 */
var invertTree = function (root) {
  const stack = [root];
  while (stack.length) {
    let n = stack.pop();
    if (n) {
      let temp = n.left;
      n.left = n.right;
      n.right = temp;
      stack.push(n.left, n.right);
    }
  }
  return root;
};
