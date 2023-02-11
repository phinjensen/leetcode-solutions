/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// I had no hope for this one... Stole this solution almost exactly from a C++ one. It's O(n^2) time and O(n?) space. Basic idea is this:
// 1. Sort the list
// 2. Iterate over every number, taking its opposite as the target.
// 3. Create two pointers, one as the next number and the other as the last in the list.
// 4. Move the pointers towards each other (because the numbers are sorted, we can use the sum and target to determine which one to move)
// 5. Once they join in the middle, add the 3 numbers as a result.
// 6. Move the front pointer and then the back pointer to a new number (to avoid duplicate entries).
// 7. Repeat until front and back meet.
// 8. Once front and back meet, we move to the next unique number in the list.
// 9. Repeat until the end of the list.
var threeSum = function (nums) {
  let result = [];
  nums.sort((a, b) => a - b);
  for (let i = 0; i < nums.length; i++) {
    let target = -nums[i];
    let front = i + 1;
    let back = nums.length - 1;
    while (front < back) {
      let sum = nums[front] + nums[back];
      if (sum < target) {
        front++;
      } else if (sum > target) {
        back--;
      } else {
        let triplet = [nums[i], nums[front], nums[back]];
        result.push(triplet);
        while (front < back && nums[front] === triplet[1]) front++;
        while (front < back && nums[back] === triplet[2]) back--;
      }
    }

    while (i + 1 < nums.length && nums[i] === nums[i + 1]) i++;
  }
  return result;
};
