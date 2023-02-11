# So much harder than it felt, but slowing down and writing things down helped. O(n) time and space complexity
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        slow = fast = head
        length = 0
        while fast:
            length += 1
            stack.append(slow)
            slow = slow.next
            fast = fast.next
            if fast:
                fast = fast.next
                length += 1

        node = None
        if length % 2:
            node = stack.pop()
            node.next = None

        while stack:
            _next = slow.next
            slow.next = node
            node = stack.pop()
            node.next = slow
            slow = _next
