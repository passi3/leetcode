"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        visited = []
        def visiting(curr: 'Node') -> None:
            if curr is None:
                return

            visited.append(curr.val)
            
            for child in curr.children or []:
                visiting(child)
        visiting(root)
        return visited