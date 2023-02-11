# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getValue(self, node):
        if node:
            return node.val
        return 0

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        prev = None
        while l1 or l2:
            _sum = self.getValue(l1) + self.getValue(l2) + carry
            node = ListNode(_sum % 10)
            carry = _sum // 10
            if prev:
                prev.next = node
            else:
                head = node
            prev = node
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            prev.next = ListNode(carry)
        return head
