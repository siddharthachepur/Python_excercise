# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
#       Recursive method
        if root is not None:
            it = self.invertTree
            right = it(root.right)
            left = it(root.left)
            root.left = right
            root.right = left
            return root
# iterative method
#        stack = [root]
#        while stack:
#            node = stack.pop()
#            if node:
#                node.left,node.right = node.right, node.left
#                stack += node.left, node.right
#        return root
