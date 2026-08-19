    # Definition for a binary tree node.
    # class TreeNode:
    #     def __init__(self, val=0, left=None, right=None):
    #         self.val = val
    #         self.left = left
    #         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0

            leftSum = dfs(node.left)
            rightSum = dfs(node.right)

            self.res += abs(leftSum - rightSum)

            return leftSum + rightSum + node.val
        
        dfs(root)
        return self.res
