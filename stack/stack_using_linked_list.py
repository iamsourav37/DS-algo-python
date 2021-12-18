

class Node:
    def __init__(self, data=None, link=None):
        self.data = data
        self.link = link

    def set_data(self, data):
        self.data = data

    def set_link(self, link):
        self.link = link


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        self.head = Node(data, self.head)

    def pop(self):
        if self.is_empty():
            print("Stack is underflow")
            return

        popped_node = self.head
        self.head = self.head.link
        return popped_node.data

    def show(self):
        if self.is_empty():
            print("Stack is underflow")
            return

        iter = self.head
        while iter:
            print(iter.data)
            iter = iter.link


stack = Stack()

stack.pop()
stack.push(12)
stack.push(2)
stack.push(78)
stack.push(45)
stack.push(43)
stack.push(23)
stack.push(21)

stack.show()

print("pop : ", stack.pop())
print("pop : ", stack.pop())
print("pop : ", stack.pop())
print("pop : ", stack.pop())
stack.show()


