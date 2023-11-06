class BinaryTree:
    class _Node:
        __slots__ = "element", "left", "right"

        def __init__(self, element, left, right):
            self.element = element
            self.left = left
            self.right = right

    def __init__(self):
        self._root = None


if __name__ == "__main__":
    print("tree")
