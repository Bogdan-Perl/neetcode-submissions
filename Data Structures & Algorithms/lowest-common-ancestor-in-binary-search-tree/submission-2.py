# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None
        if not root:
            return None
        if root.val > p.val and root.val > q.val:
            L = self.lowestCommonAncestor(root.left, p, q)
            res = L if L else res
        elif root.val < p.val and root.val < q.val:
            R = self.lowestCommonAncestor(root.right, p, q)
            res = R if R else res
        else:
            return root


        return res



        