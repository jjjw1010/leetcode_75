# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root
        # Binary Search Tree Rule:
        # Left Subtree < Right Subtree in vals
        while node:
            # if p and q are less than node.val, go left
            if p.val < node.val and q.val < node.val:
                node = node.left
            # if p and q are greater than node.val, go right
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else:
                # stop. You found the Lowest Common Ancestor
                return node