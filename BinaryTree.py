class BinaryTree:

    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print node.data,
            self.inorder(node.right)

    def preorder(self, node):
        if node is not None:
            print node.data,
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print node.data,

root = BinaryTree(50)
root.left = BinaryTree(25, BinaryTree(10), BinaryTree(40))
root.right = BinaryTree(75)

root.inorder(root)
print
root.preorder(root)
print
root.postorder(root)
print
