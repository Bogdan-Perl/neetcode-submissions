# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(root, orginal):
            if not orginal:
                return None
            
            root =  TreeNode(orginal.val)
            root.left = invert(root.left, orginal.right)
            root.right = invert(root.right, orginal.left)

            return root
        
        return invert(None, root)
