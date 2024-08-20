# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        temp = 0

        while l1 or l2 or temp:
            val_l1 = l1.val if l1 else 0
            val_l2 = l2.val if l2 else 0
            sum_val = val_l1 + val_l2 + temp
            temp = sum_val // 10

            current.next = ListNode(sum_val % 10)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next