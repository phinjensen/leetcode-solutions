/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function (arr, fn) {
  const result = [];
  for (const [i, el] of arr.entries()) {
    if (fn(el, i)) {
      result.push(el);
    }
  }
  return result;
};
