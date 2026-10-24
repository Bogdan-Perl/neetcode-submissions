# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = -1

        def inOrder(root):
            nonlocal cnt, res
            if not root:
                return
            inOrder(root.left)
            if cnt == 1:
                res = root.val
                cnt -= 1
                return
            cnt -= 1
            inOrder(root.right)

        inOrder(root)
        return res

