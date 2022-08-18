class BinaryNode:
    def __init__(self, left, data, right):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        If the root is empty, make the root the new node. Otherwise, add the new node to the leftmost empty spot in the tree

        :param data: The data to be inserted into the tree
        """
        if self.root is None:
            self.root = BinaryNode(None, data, None)
        else:
            q = [self.root]
            while len(q) != 0:
                temp = q[0]
                q.pop(0)
                if temp.left is None:
                    temp.left = BinaryNode(None, data, None)
                    break
                elif temp.left is not None:
                    q.append(temp.left)
                if temp.right is None:
                    temp.right = BinaryNode(None, data, None)
                    break
                elif temp.right is not None:
                    q.append(temp.right)

    def inorder(self, temp):
        """
        If the current node is not empty, then recursively traverse the left subtree, print the data of the current node,
        and recursively traverse the right subtree

        :param temp: The node to be traversed
        :return: The inorder traversal of the tree.
        """
        if not temp:
            return
        self.inorder(temp.left)
        print(temp.data, end=" ")
        self.inorder(temp.right)

    def preorder(self, temp):
        """
        If the current node is not empty, print the current node's data, then recursively call the preorder function on the
        left and right children of the current node

        :param temp: The node to be visited
        :return: The preorder traversal of the tree.
        """
        if not temp:
            return
        print(temp.data, end=" ")
        self.preorder(temp.left)
        self.preorder(temp.right)

    def postorder(self, temp):
        """
        We are traversing the left subtree, then the right subtree, and then printing the data of the root node

        :param temp: The node to be visited
        :return: The postorder traversal of the tree.
        """
        if not temp:
            return
        self.postorder(temp.left)
        self.postorder(temp.right)
        print(temp.data, end=" ")


tree = BinaryTree()
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)
tree.insert(8)
tree.insert(9)
print("Pre-Order print", end="\n")
tree.preorder(tree.root)  # DLR
print()
print("In-Order print", end="\n")
tree.inorder(tree.root)  # LDR
print()
print("Post-Order print", end="\n")
tree.postorder(tree.root)  # LRD
#             1
#          /     \
#         2        3
#       /   \     /   \
#     4      5   6     7
#   /  \
# 8     9
