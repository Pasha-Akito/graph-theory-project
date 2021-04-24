# Adapted from pseudocode at:
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Convert infix expressions to postfix"""
    # the eventual output.
    postfix = ""
    # The shunting yard operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 100, '/': 90, '+': 80, '-': 70}
    # Loop through the input a character at a time
    for c in infix:
        # c is a digit
        if c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            # Push it to the output
            postfix = postfix + c
        # c is an operator
        elif c in {'+', '-', '*', '/'}:
            # Check what is on the stack.
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] > prec[c]:
                # Move operator at top of stack to output
                postfix = postfix + stack[-1]
                # Remove operator from stack
                stack = stack[:-1]
            # Push c to the stack.
            stack = stack + c
        elif c == '(':
            # Push c to the stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove left bracket from stack
            stack = stack[:-1]
    while len(stack) != 0:
        # Append operator at top of stack to output.
        postfix = postfix + stack[-1]
        # Remove operator from stack.
        stack = stack[:-1]
    return postfix



infix = "3+4*(2-1)"
postfix = "3421-*+"

print(f"{infix} - > {shunt(infix)}")

if __name__ == "__main__":
    for infix in ["a.(b.b)*.a", "1.(0.0)*.1"]:
        print(f"infix:   {infix}")
        print(f"postfix: {shunt(infix)}")
        print()