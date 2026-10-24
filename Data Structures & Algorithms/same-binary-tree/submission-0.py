# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        res = True
        leftTree = self.isSameTree(p.left, q.left)
        if p.val != q.val:
            res = False
        rightTree = self.isSameTree(p.right, q.right)

        return leftTree and rightTree and res

        