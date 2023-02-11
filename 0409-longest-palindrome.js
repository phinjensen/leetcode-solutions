/**
 * @param {string} s
 * @return {number}
 */
// Time complexity: O(n)
// Space complexity O(m) where m is the alphabet size. Could also be considered O(1) for a given alphabet, but this algorithm works for any, hence the second parameter m.
var longestPalindrome = function (s) {
  const letters = {};
  for (let c of s) {
    if (typeof letters[c] === "undefined") letters[c] = 1;
    else letters[c] += 1;
  }
  let single = false,
    total = 0;
  for (let c of Object.keys(letters)) {
    if (letters[c] % 2 === 1) {
      if (!single) {
        single = true;
      } else {
        letters[c] -= 1;
      }
    }
    total += letters[c];
  }
  return total;
};
