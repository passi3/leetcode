# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # reculsive DFS
        if root is None:
            return True
        return self.innerSymmetric(root.left, root.right)
        
    def innerSymmetric(self, left, right):
        if not left and not right:
            return True
        elif not left or not right:
            return False
        elif left.val != right.val:
            return False
        
        return self.innerSymmetric(left.left, right.right) and self.innerSymmetric(left.right, right.left)