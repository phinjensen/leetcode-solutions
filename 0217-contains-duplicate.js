/**
 * @param {number[]} nums
 * @return {boolean}
 */
// Easy O(n) time & space.
var containsDuplicate = function (nums) {
  let cache = {};
  for (let num of nums) {
    if (cache[num]) return true;
    else cache[num] = true;
  }
  return false;
};
