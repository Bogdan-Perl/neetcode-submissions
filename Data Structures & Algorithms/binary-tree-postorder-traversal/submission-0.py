# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        vist = [False]
        res = []

        while stack:
            curr, visted = stack.pop(), vist.pop()
            if curr:
                if visted:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    vist.append(True)
                    stack.append(curr.right)
                    vist.append(False)
                    stack.append(curr.left)
                    vist.append(False)
        return res