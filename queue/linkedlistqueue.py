"""
ADT

Node
first (front)
isEmpty
enqueue
dequeue
"""


class SingleListQueue:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._front = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, element):
        if self.isEmpty():
            self._front = self._Node(element, None)
