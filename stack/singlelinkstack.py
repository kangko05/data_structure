"""
ADT

top = head

isEmpty
push
pop
top (=peek)

all the operations are O(1)
=> because the removal of data only occurs at the top(head)
"""
import random


class Empty(Exception):
    pass


class LinkedStack:
    class _Node:
        __slots__ = "element", "next"

        def __init__(self, element, next):
            self.element = element
            self.next = next

    def __init__(self):
        self._head = None  # this represents top of the stack
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def push(self, element):
        self._head = self._Node(element, self._head)
        self._size += 1

    def top(self):
        if self.isEmpty():
            raise (Empty("Stack is empty"))
        return self._head.element

    def pop(self):
        if self.isEmpty():
            raise (Empty("Stack is empty"))

        ret = self._head.element
        self._head = self._head.next
        self._size -= 1

        return ret


if __name__ == "__main__":
    lst = LinkedStack()

    print(lst.isEmpty())
    print(len(lst))

    for i in range(12):
        lst.push(random.randint(0, 100))

    for i in range(12):
        print(lst.top())

    print(lst.isEmpty())
    print(len(lst))

    while not lst.isEmpty():
        print(lst.pop())

    print(len(lst))
    print(lst.isEmpty())
