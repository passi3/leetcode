# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False    # 빈 노드는 False 반환
        
        if root.left == None and root.right == None and root.val == targetSum:
            return True # 현재 노드가 leaf이고 값이 targetSum과 같은 경우 True 반환

        return self.hasPathSum(root.left, targetSum-root.val) or self.hasPathSum(root.right, targetSum-root.val)    # recursive로 root의 왼쪽 또는 오른쪽 노드 호출하며, 그때의 target 값을 현재 노드의 값을 뺌으로써 업데이트