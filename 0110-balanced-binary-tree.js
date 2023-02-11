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
 * @return {boolean}
 */

// Failed to do this one on my own. I had some good ideas but got intimidated by the hidden complexity of it.
// This solution bascially usese recursion to get to the bottom of each branch and then builds the height for
// each node as it goes back up, but checks if the height difference is greater than 1 for every node. If it
// ever is, it passes that information all the way back and we can check it for the root node.
//
// Time complexity is O(n). Space complexity is O(1).

let height = function (root) {
  if (!root) return 0;
  const left = height(root.left),
    right = height(root.right);
  if (left === -1 || right === -1 || Math.abs(left - right) > 1) return -1;
  return Math.max(left, right) + 1;
};

var isBalanced = function (root) {
  return height(root) != -1;
};
