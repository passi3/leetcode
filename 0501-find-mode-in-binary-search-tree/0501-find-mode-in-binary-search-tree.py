# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.cnt = 0
        self.maxCnt = 0
        self.res = []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return
            
            dfs(node.left)

            if self.prev == node.val:
                self.cnt += 1
            else:
                self.prev = node.val
                self.cnt = 1

            if self.cnt > self.maxCnt:
                self.maxCnt = self.cnt
                self.res = [node.val]
            elif self.cnt == self.maxCnt:
                self.res.append(node.val)
            
            dfs(node.right)
        
        dfs(root)
        return self.res