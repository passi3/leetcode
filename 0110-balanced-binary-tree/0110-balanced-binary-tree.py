# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check(self, root):
        if root is None:
            return 0  # 빈 노드는 깊이 0을 반환
        
        left_depth = self.check(root.left)
        if left_depth == -1:  # 왼쪽 서브트리가 균형 잡히지 않은 경우
            return -1
        
        right_depth = self.check(root.right)
        if right_depth == -1:  # 오른쪽 서브트리가 균형 잡히지 않은 경우
            return -1
        
        if abs(left_depth - right_depth) >= 2:
            return -1  # 현재 서브트리가 균형 잡히지 않은 경우
        
        return max(left_depth, right_depth) + 1  # 현재 서브트리의 깊이 반환

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.check(root) != -1