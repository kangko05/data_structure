"""
ADT

Node
first (front)
isEmpty
enqueue
dequeue
rotate
"""

from random import randint


class CircularQueue:
    class _Node:
        __slots__ = "element", "next"

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._tail = None  # head = tail.next
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, e):
        newNode = self._Node(e, None)
        if self.isEmpty():
            newNode.next = newNode  # new node = head & tail at the same time
        else:
            newNode.next = self._tail.next  # new node.next = head
            self._tail.next = newNode
        self._tail = newNode
        self._size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")

        oldHead = self._tail.next

        if self._size == 1:
            self._tail = None
        else:
            self._tail.next = oldHead.next

        self._size -= 1

        return oldHead.element

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail.next

    def show(self):
        if self._size > 0:
            curr = self._tail.next
            while curr.next != self._tail.next:  # breaks out when curr = tail
                print(curr.element)
                curr = curr.next

            print(self._tail.element)


if __name__ == "__main__":
    scq = CircularQueue()

    print("empty length: ", len(scq))

    for _ in range(12):
        scq.enqueue(randint(0, 100))

    print("pushed 12 elements length: ", len(scq))

    for _ in range(5):
        print(scq.dequeue())

    print("dequeued 5 elements length:  ", len(scq))

    scq.show()
