# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        q = deque([root])

        while q:
            level = len(q)
            vals = 0

            for _ in range(level):
                node = q.popleft()
                vals += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            res.append(vals/level)
        return res