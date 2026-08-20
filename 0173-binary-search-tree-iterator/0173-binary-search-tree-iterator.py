# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.curr = 0
        self.vals = []

        def inOrder(root):
            if root:
                inOrder(root.left)
                self.vals.append(root.val)
                inOrder(root.right)
        
        inOrder(root)

    def next(self) -> int:
        res = self.vals[self.curr]
        self.curr += 1
        return res

    def hasNext(self) -> bool:
        return self.curr < len(self.vals)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()