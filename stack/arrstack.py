"""
ADT

top

1. push
2. pop
3. isEmpty
4. isFull
5. peek
"""


class ArrStack:
    def __init__(self, capacity: int):
        self._cap = capacity
        self._items = [None] * self._cap
        self._top = -1

    def isEmpty(self) -> bool:
        return True if self._top < 0 else False

    def isFull(self) -> bool:
        return True if self._top >= self._cap - 1 else False

    def push(self, item):
        if not self.isFull():
            self._top += 1
            self._items[self._top] = item
        else:
            print("[push]the stack is full")

    def pop(self):
        if not self.isEmpty():
            self._top -= 1
            return self._items[self._top + 1]
        else:
            print("[pop]the stack is empty")

    def peek(self):
        if not self.isEmpty():
            return self._items[self._top]
        else:
            print("[peek]the stack is empty")


if __name__ == "__main__":
    ast = ArrStack(10)

    print(ast.isEmpty())
    print(ast.isFull())

    for i in range(15):
        ast.push(i)

    print(ast.isEmpty())
    print(ast.isFull())

    while not ast.isEmpty():
        print(ast.pop())

    ast.pop()
    ast.push(352)

    print(ast.peek())
    ast.pop()
    ast.peek()
