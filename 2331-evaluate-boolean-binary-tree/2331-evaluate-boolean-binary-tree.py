# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def postorder(node: Optional[TreeNode]):
            if node.left is None and node.right is None:
                return bool(node.val)
            
            if node.val == 2:
                return postorder(node.left) or postorder(node.right)
            else:
                return postorder(node.left) and postorder(node.right)
        
        return postorder(root)