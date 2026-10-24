# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.resNode = None

        def dfs(root, p, q) -> bool:
            if not root:
                return False

            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            if (left or right) and not (left and right) and not self.resNode and ( p == root.val or q == root.val) :
                self.resNode = root
            if p == root.val or q == root.val:
                return True
            if left and right and not self.resNode:
                self.resNode = root
            return left or right
        dfs(root, p.val, q.val)
        return self.resNode