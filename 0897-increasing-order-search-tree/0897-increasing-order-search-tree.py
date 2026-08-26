# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(node: Optional[TreeNode]):
            nonlocal prev
            if not node:
                return
            inorder(node.left)

            node.left = None
            prev.right = node
            prev = node

            inorder(node.right)
        
        dummy = TreeNode(0)
        prev = dummy
        inorder(root)

        return dummy.right