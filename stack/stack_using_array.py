import numpy as np


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack_array = np.empty(self.capacity, dtype="int64")
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity-1

    def push(self, data):
        if self.is_full():
            print("Stack Overflow")
            return
        self.top += 1
        self.stack_array[self.top] = data

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return
        popped_value = self.stack_array[self.top]
        self.top -= 1

    def show(self):
        if self.is_empty():
            print("Stack underflow")
            return

        for i in range(self.top, -1, -1):
            print(self.stack_array[i])



stack = Stack(4)
stack.pop()
stack.push(78)
stack.push(8)
stack.push(18)
stack.push(98)
stack.push(-9)
stack.show()
