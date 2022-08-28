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
// Initial attempt, O(n) time and O(1) space.
var reverseList = function(head) {
    let prev = null;
    let node = head;
    let next = node?.next;
    while (node) {
        next = node.next;
        node.next = prev;
        prev = node;
        node = next;
    }
    return prev;
};


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
// Second attempt, still the same time complexity. More clear what's going on, IMO, but performance of destructuring is probably different.
var reverseList = function (head) {
  let [prev, curr] = [null, head];
  while (curr) {
    [curr.next, prev, curr] = [prev, curr, curr.next];
  }
  return prev;
};
