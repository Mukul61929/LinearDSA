def are_brackets_closed(code_snippet):
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in code_snippet:
        if char in '({[':
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in ')}]':
            # If the character is a closing bracket
            if not stack or stack.pop() != bracket_pairs[char]:
                # If the stack is empty or the popped bracket doesn't match
                return False

    # If the stack is empty, all brackets are closed properly
    return not stack


code = "{[()]}"
result = are_brackets_closed(code)

if result:
    print("All brackets are closed properly.")
else:
    print("Brackets are not closed properly.")
