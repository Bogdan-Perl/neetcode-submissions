# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(root, subRoot):
            if not root and not subRoot:
                return True
            if not root or not subRoot:
                return False
            
            check = root.val == subRoot.val
            check = check and isEqual(root.left, subRoot.left)
            check = check and isEqual(root.right, subRoot.right)

            return check

        stack = []
        res = False
        while stack or root:
            while root:
                stack.append(root)
                res = res or isEqual(root, subRoot)
                root = root.left
            root = stack.pop()
            root = root.right

        
        return res
