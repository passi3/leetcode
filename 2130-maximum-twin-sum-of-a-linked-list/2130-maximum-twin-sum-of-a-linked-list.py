# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = 0
        n = 0
        curr = head

        while curr:
            n += 1
            curr = curr.next
        
        stack = []
        curr = head

        for _ in range(n//2):
            stack.append(curr.val)
            curr = curr.next
        
        while curr:
            res = max(res, curr.val + stack.pop())
            curr = curr.next
        
        return res