# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        res = 0

        def dfs(node: Optional[TreeNode]) -> tuple[int, int]:
            nonlocal res

            if node is None:
                return 0, 0
            
            l_sum, l_cnt = dfs(node.left)
            r_sum, r_cnt = dfs(node.right)
            
            total_sum = l_sum + r_sum + node.val
            total_cnt = l_cnt + r_cnt + 1

            if total_sum // total_cnt == node.val:
                res += 1
            
            return total_sum, total_cnt
        
        dfs(root)

        return res