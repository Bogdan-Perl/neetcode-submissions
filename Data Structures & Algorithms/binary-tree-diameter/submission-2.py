# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(root):
            if not root:
                return 0
            
            lh = dfs(root.left) 
            rh = dfs(root.right) 
            diameter = lh + rh
            if diameter > self.res:
                self.res = diameter

            return max(lh, rh) + 1
        dfs(root)
        return self.res