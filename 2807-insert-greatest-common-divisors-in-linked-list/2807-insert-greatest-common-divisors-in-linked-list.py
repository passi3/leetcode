# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next is not None:
            nxt = curr.next
            d = gcd(curr.val, nxt.val)
            newNode = ListNode(d, next=nxt)
            curr.next = newNode

            curr = nxt
        
        return head
            