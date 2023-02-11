/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
// O(n) time, O(1) space. Idea is going through from top left to bottom right,
// taking the best so far from the left and upper coordinates, and then doing
// the same starting from the bottom right taking the left and below options.
// The second run, don't take an option if it's worse than what we have.
var updateMatrix = function (mat) {
  for (let i = 0; i < mat.length; i++) {
    let r = mat[i];
    for (let j = 0; j < r.length; j++) {
      if (r[j]) {
        r[j] = 1 + Math.min(r[j - 1] ?? Infinity, mat[i - 1]?.[j] ?? Infinity);
      }
    }
  }
  for (let i = mat.length - 1; i >= 0; i--) {
    let r = mat[i];
    for (let j = r.length - 1; j >= 0; j--) {
      if (r[j]) {
        r[j] = Math.min(
          r[j],
          1 + Math.min(r[j + 1] ?? Infinity, mat[i + 1]?.[j] ?? Infinity)
        );
      }
    }
  }
  return mat;
};
