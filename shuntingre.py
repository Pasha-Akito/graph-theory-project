# Adapted from pseudocode at:
# https://en.wikipedia.org/wiki/Shunting-yard_algorithm

def shunt(infix):
    """Convert infix expressions to postfix"""
    # The eventual output.
    postfix = ""
    #The shunting yard operator stack.
    stack = ""
    # Operator precedence.
    prec = {'*': 100, '.': 90, '|': 80}
    # Loop through the input a character at a time
    for c in infix:
        # If c is a non-special
        if c in {'*', '.', '|'}:
            #Check what is on the stack. \ contuines code from above
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] >= prec[c]:
                # Append opperator at top of the stack to output.
                postfix = postfix + stack[-1]
                #Remove operator from the stack
                stack = stack[:-1]
            # push c to stack
            stack = stack + c
        elif c == '(':
            # push c to stack
            stack = stack + c
        elif c == ')':
            while stack[-1] != '(':
                # Append operator at top of the stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from the stack
                stack = stack[:-1]
            # Remove open bracket stack.
            stack = stack[:-1]
        #Empty the operator stack
        else:
            #push it to the output
            postfix = postfix + c
    
    #Empty the operator stack
    while len(stack) != 0:
        # Append operator at top of the stack to output.
        postfix = postfix + stack[-1]
        #Remove operator from the stack.
        stack = stack[:-1]
    #return the postfix version of infix 
    return postfix

if __name__ == "__main__":
    for infix in ["a.(b.b)*.a", "1.(0.0)*.1"]:
        print(f"infix: {infix}")
        print(f"postfix: {shunt(infix)}")
        print()
