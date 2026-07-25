# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        nodes = []
        
        while True:
            n+= 1
            nodes.append(head)

            if head.next == None:
                break

            head = head.next
        
        return nodes[n//2]