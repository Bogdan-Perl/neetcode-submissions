# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 0
        def dfs(node, currMax):
            nonlocal goodNodes
            if not node:
                return
            if node.val >= currMax:
                currMax = node.val
                goodNodes += 1
            dfs(node.left, currMax)
            dfs(node.right, currMax)
        dfs(root, float('-inf'))
        return goodNodes
            
