/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
// Improvement on solution below, just because we don't have to worry about counting. Just move one pointer twice as fast as the other!
// Inspired not by looking at code, but by seeing "fast/slow pointers" in the discussions lists
var middleNode = function (head) {
  let mid = head;
  let curr = head.next;
  while (curr) {
    curr = curr.next?.next;
    mid = mid.next;
  }
  return mid;
};

// Same time complexity, but I think it's slightly slower (not significantly, though). More importantly, it's just a bit more complex to read.
var middleNode = function (head) {
  let i = 0;
  let mid = head;
  let curr = head;
  while (curr) {
    curr = curr.next;
    if (i % 2 == 0) {
      mid = mid.next;
    }
    i++;
  }
  return mid;
};
