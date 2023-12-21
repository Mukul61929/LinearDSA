def is_operator(char):
    return char in {'+', '-', '*', '/'}

def postfix_to_prefix(postfix_expression):
    stack = []

    for char in postfix_expression:
        if not is_operator(char):
            # If the character is an operand, push it to the stack
            stack.append(char)
        else:
            # If the character is an operator, pop two operands from the stack
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Construct the new operand by concatenating the operator and operands
            new_operand = char + operand1 + operand2

            # Push the new operand back to the stack
            stack.append(new_operand)

    # The final result is the top of the stack
    return stack.pop()


postfix_expression = "23+5*"
prefix_expression = postfix_to_prefix(postfix_expression)

print(f"Postfix Expression: {postfix_expression}")
print(f"Prefix Expression: {prefix_expression}")
