/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */

// I kinda peeked a look at the discussions but they really just made me think "I can figure this out". I did, but it's
// ugly. It does work, though, and it's linear time.

var addBinary = function (a, b) {
  let carry = false;
  let i = 1;
  let result = "";
  while (i <= a.length || i <= b.length) {
    let x = a[a.length - i] || "0",
      y = b[b.length - i] || "0";
    if (x == "1" && y == "1") {
      if (carry) {
        result += "1";
      } else {
        result += "0";
        carry = true;
      }
    } else if (x == "1" || y == "1") {
      if (carry) {
        result += "0";
      } else {
        result += "1";
      }
    } else {
      if (carry) {
        result += 1;
        carry = false;
      } else {
        result += "0";
      }
    }
    i++;
  }
  if (carry) result += "1";
  return [...result].reverse().join("");
};
