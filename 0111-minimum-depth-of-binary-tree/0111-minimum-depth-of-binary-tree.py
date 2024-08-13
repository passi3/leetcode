# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0 # 빈 노드는 깊이 0 반환
        
        if not root.left and not root.right:
            return 1 # 루트가 리프 노드인 경우

        if not root.right:
            return 1 + self.minDepth(root.left) # 왼쪽 노드만 자식을 가지고 있을 경우

        if not root.left:
            return 1 + self.minDepth(root.right) # 오른쪽 노드만 자식을 가지고 있을 경우

        return 1 + min(self.minDepth(root.left), self.minDepth(root.right)) # 양쪽 노드 모두 자식을 가지고 있을 경우