def is_operator(char):
    return char in {'+', '-', '*', '/'}

def prefix_to_infix(prefix_expression):
    stack = []

    # Traverse the prefix expression in reverse order
    for char in reversed(prefix_expression):
        if not is_operator(char):
            # If the character is an operand, push it to the stack
            stack.append(char)
        else:
            # If the character is an operator, pop two operands from the stack
            operand1 = stack.pop()
            operand2 = stack.pop()

            # Construct the new operand by concatenating operands, operator, and parentheses
            new_operand = f"({operand1}{char}{operand2})"

            # Push the new operand back to the stack
            stack.append(new_operand)

    # The final result is the top of the stack
    return stack.pop()


prefix_expression = "*+AB-CD"
infix_expression = prefix_to_infix(prefix_expression)

print(f"Prefix Expression: {prefix_expression}")
print(f"Infix Expression: {infix_expression}")
