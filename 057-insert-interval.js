/**
 * @param {number[][]} intervals
 * @param {number[]} newInterval
 * @return {number[][]}
 */

// Failed to do this on my own. I could kinda get it but it failed with edge cases. 
// O(n) time and space
var insert = function(intervals, newInterval) {
    if (intervals.length === 0) {
        return [newInterval];
    }
    let [start, end] = newInterval;
    let left = intervals.filter(i => i[1] < start);
    let right = intervals.filter(i => i[0] > end);
    if (left.length + right.length !== intervals.length) {
        start = Math.min(intervals[left.length][0], start);
        end = Math.max(intervals[intervals.length - right.length - 1][1], end);
    }
    return left.concat([[start, end]]).concat(right);
};
