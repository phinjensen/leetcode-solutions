/**
 * @param {number[]} nums
 * @return {number}
 */
// Time O(n) space O(1). Didn't solve it myself, instead I referenced
// [this discussion](https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution).
// A commenter points out that this is the [Boyer-Moore Majority Vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm).
var majorityElement = function (nums) {
  let major = nums[0],
    count = 1;
  for (let n of nums.slice(1)) {
    if (count === 0) {
      major = n;
      count++;
    } else if (major == n) {
      count++;
    } else {
      count--;
    }
  }
  return major;
};
