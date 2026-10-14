# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            # we know to search right if both are greater than root
            if p.val > root.val and q.val > root.val:
                root = root.right
            # we know to search left if both are less
            elif p.val < root.val and q.val < root.val:
                root = root.left
            # if they're split (like p = 3, q = 8) then it has to be root
            else:
                return root

        