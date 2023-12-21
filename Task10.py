class StackWithMin:
    def __init__(self):
        self.stack = []  # Main stack to store elements
        self.min_stack = []  # Auxiliary stack to store minimum elements

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        # If the min_stack is empty or the new item is smaller than the current minimum,
        # push the new item onto the min_stack.
        if len(self.min_stack) == 0 or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.is_empty():
            # If the popped item from the main stack is the minimum, also pop from the min_stack.
            if self.stack[-1] == self.min_stack[-1]:
                self.min_stack.pop()
            return self.stack.pop()

    def get_min(self):
        if not self.is_empty():
            return self.min_stack[-1]

stack_with_min = StackWithMin()

# Push elements onto the stack
stack_with_min.push(3)
stack_with_min.push(5)
stack_with_min.push(2)
stack_with_min.push(8)
stack_with_min.push(1)

print("Current Stack:", stack_with_min.stack)
print("Smallest Number:", stack_with_min.get_min())

# Pop an element
stack_with_min.pop()

print("After Popping an Element:")
print("Current Stack:", stack_with_min.stack)
print("Smallest Number:", stack_with_min.get_min())
