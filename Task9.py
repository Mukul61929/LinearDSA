class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

def reverse_stack(stack):
    aux_stack = Stack()

    # Push elements from the original stack to the auxiliary stack
    while not stack.is_empty():
        aux_stack.push(stack.pop())

    # Push elements back to the original stack (reversing them)
    while not aux_stack.is_empty():
        stack.push(aux_stack.pop())


original_stack = Stack()
for item in [1, 2, 3, 4, 5]:
    original_stack.push(item)

print("Original Stack:", original_stack.items)

reverse_stack(original_stack)

print("Reversed Stack:", original_stack.items)
