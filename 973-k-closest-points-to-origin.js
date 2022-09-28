/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */

// O(n log n) although it technically depends on the sorting algorithm which isn't specified by ECMAScript. There
// are lots of other ways of doing it in the discussions, including max heap and quicksort inspired ways.

function dist([a, b]) {
  return Math.sqrt(a * a + b * b);
}

var kClosest = function (points, k) {
  points.sort((a, b) => dist(a) - dist(b));
  return points.slice(0, k);
};
