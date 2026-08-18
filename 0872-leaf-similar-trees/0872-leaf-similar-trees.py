# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def getLeaves(node: Optional[TreeNode]) -> list[int]:
            leaves = []

            def dfs(node: Optional[TreeNode]):
                if node is None:
                    return
                if node.left is None and node.right is None:
                    leaves.append(node.val)
                    return
                dfs(node.left)
                dfs(node.right)
            
            dfs(node)
            return leaves
        
        return getLeaves(root1) == getLeaves(root2)