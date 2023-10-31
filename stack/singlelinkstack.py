"""
ADT

top = tail

isEmpty
push
pop
top (=peek)

"""
import random


class LinkedStack:
    class _Node:
        __slots__ = "_element", "_next"

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        tmp = self._head._element
        self._head = self._head._next
        self._size -= 1
        return tmp

    def peek(self):
        if self.isEmpty():
            raise IndexError("Stacak is empty")
        return self._head._element


if __name__ == "__main__":
    lst = LinkedStack()

    print(lst.isEmpty())
    print(len(lst))

    for i in range(12):
        lst.push(random.randint(0, 100))

    print(len(lst))

    for i in range(12):
        print(lst.peek())

    print(lst.isEmpty())
    print(len(lst))

    while not lst.isEmpty():
        print(lst.pop())

    print(len(lst))
    print(lst.isEmpty())
