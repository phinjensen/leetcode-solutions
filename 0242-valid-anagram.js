/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
// Time complexity of .sort() not specified in the ECMA specification, but generally will use O(n log n).
// Firefox uses merge sort, Chrome uses timsort, which has a lower bound of O(n).
// Space complexity here would be O(n).
var isAnagram = function (s, t) {
  s = [...s].sort().join("");
  t = [...t].sort().join("");
  return t === s;
};

// Time complexity of O(n), space complexity O(n).
var isAnagram = function (s, t) {
  let d = {};
  if (s.length !== t.length) return false;
  for (let char of s) {
    if (d[char]) d[char]++;
    else d[char] = 1;
  }
  for (let char of t) {
    if (d[char]) d[char]--;
    else return false;
  }
  return Object.values(d).every((val) => val === 0);
};
