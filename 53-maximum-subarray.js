/**
 * @param {number[]} nums
 * @return {number}
 */
// An O(n) solution I came up with on my own! Uses an approach similar to that of https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
// where you keep track of the lowest number seen so far and highest difference as you walk through the list. To make that work here, I just
// had to convert the array to a list of "current number if all were numbers were summed so far" and then find the greatest difference between
// two numbers in that array.
var maxSubArray = function (nums) {
  let curr = 0;
  for (let i = 0; i < nums.length; i++) {
    curr += nums[i];
    nums[i] = curr;
  }
  let min = 0,
    max = -Infinity;
  for (let num of nums) {
    if (num - min > max) {
      max = num - min;
    }
    if (num < min) {
      min = num;
    }
  }
  return max;
};

// Dynamic programming solutino using O(n) time and space complexity. Written by myself with no direct help, but influenced by a solution I read
// twelve days ago (judging by LeetCode submission dates) after doing the above solution. This solution creates an array of the maximum subarray
// *ending* at each point rather by taking the maximum of the best from the previous index + the value at the current index or the current index
// alone. The highest value calculated along the way is our answer.
var maxSubArray = function (nums) {
  s = new Array(nums.length + 1);
  s[0] = 0;
  let max = -Infinity;
  for (let i = 0; i < nums.length; i++) {
    s[i + 1] = Math.max(nums[i] + s[i], nums[i]);
    max = Math.max(s[i + 1], max);
  }
  return max;
};
