/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
// O(log n) time, O(1) space. Original approach used `min + Math.floor((max - min) /2)` and
// checked nums[i] === target before the > and <, but was significantly slower (at least in
// the Leetcode scheme of things).
var search = function (nums, target) {
  let max = nums.length - 1,
    min = 0;

  while (max >= min) {
    let i = Math.floor((min + max) / 2);
    if (nums[i] > target) max = i - 1;
    else if (nums[i] < target) min = i + 1;
    else return i;
  }
  return -1;
};
