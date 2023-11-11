"""
binary tree can be implemented based on either array or linked list
- array based bt can be inefficient for memory usage
- so, linked list based bt is more common than array based

ADT
1. Tree Node
    - element (or data)
    - left child node
    - right child node
2. Traversal
    - preorder
    - inorder
    - postorder
"""


class BinaryTree:
    class _Node:
        __slots__ = "element", "left", "right"

        def __init__(self, element, left, right):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self):
        self._root = None

    def preTraverse(self, node):
        if node is not None:
            print(node.element, end=" ")
            self.preTraverse(node.left)
            self.preTraverse(node.right)

    def inTraverse(self, node):
        if node is not None:
            self.preTraverse(node.left)
            print(node.element, end=" ")
            self.preTraverse(node.right)

    def postTraverse(self, node):
        if node is not None:
            self.preTraverse(node.left)
            self.preTraverse(node.right)
            print(node.element, end=" ")


class CircularQueue:
    pass


def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=" ")
            queue.enqueue(n.left)
            queue.enqueue(n.right)


if __name__ == "__main__":
    print("tree")
