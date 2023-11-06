"""
ADT

Node
first (front)
isEmpty
enqueue
dequeue
"""

import random


class LinkedQueue:
    class _Node:
        __slots__ = "element", "next"

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = None  # front
        self._tail = None  # rear
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)

        if self.isEmpty():
            self._head = newNode
        else:
            self._tail.next = newNode

        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise (IndexError("queue is empty"))

        ret = self._head.element
        self._head = self._head.next
        self._size -= 1
        return ret

    def first(self):
        if self.isEmpty():
            raise (IndexError("queue is empty"))

        return self._head.element


if __name__ == "__main__":
    print("queue with singly linked\n")

    slq = LinkedQueue()
    print("empty>> ", slq.isEmpty())
    print("len>> ", len(slq))

    for i in range(12):
        slq.enqueue(random.randint(0, 100))

    print("pushed 12 elements...")
    print("len>> ", len(slq))

    print("dequeue 10 elements")
    for i in range(10):
        print(slq.dequeue())

    print("dequeue 10 elements")
    print("len>> ", len(slq))
