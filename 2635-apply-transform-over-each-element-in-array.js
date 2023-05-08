/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function (arr, fn) {
  result = new Array(arr.length);
  for (const [i, el] of arr.entries()) {
    result[i] = fn(el, i);
  }
  return result;
};
