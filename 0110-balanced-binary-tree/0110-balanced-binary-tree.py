# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    depth = 0

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0

            left_node = dfs(node.left)
            right_node = dfs(node.right)
            self.depth = max(self.depth, abs(left_node-right_node))

            return max(left_node, right_node) + 1
        
        dfs(root)
        return self.depth < 2