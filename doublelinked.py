"""
ADT
1. insert (head/tail/middle)
2. remove (head/tail/middle)
3. search
"""


class DoubleLinkedList:
    class _Node:
        __slots__ = "element", "next", "prev"

        def __init__(self, element, next, prev):
            self.element = element
            self.next = next
            self.prev = prev

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)

        self._header.next = self._trailer
        self._trailer.prev = self._header

        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def _insertMiddle(self, element, predecessor, successor):
        newNode = self._Node(element, predecessor, successor)

        predecessor.next = newNode
        successor.prev = newNode
        self.size += 1
        return newNode

    def _deleteNode(self, node):
        predecessor = node.prev
        successor = node.next

        successor.prev = predecessor
        predecessor.next = successor

        self.size -= 1

        element = node.element

        node.next = node.prev = node.element = None

        return element


if __name__ == "__main__":
    dll = DoubleLinkedList()
    print("empty length = ", len(dll))
