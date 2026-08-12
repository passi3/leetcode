# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = 0
        prev = head
        curr = prev.next
        
        while curr:
            if curr.val == 0:
                prev.val = temp
                temp = 0

                if curr.next:
                    prev.next = curr.next
                    prev = prev.next
                else:
                    prev.next = None

            else:
                temp += curr.val

            curr = curr.next

        return head