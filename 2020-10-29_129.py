# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root) -> int:

        def dfs(node, res):
            if not node: return 0
            total = res * 10 + node.val
            if not node.left and node.right:
                return total
            else:
                return dfs(node.left, total) + dfs(node.right, total)

        if not root: return 0
        return dfs(root, 0)
