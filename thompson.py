# Thompson's construction

import shuntingre

class State():
    """A state and its arrows"""

    # Constructor
    def __init__(self, label, arrows, accept):
        """Label is the arrow labels. Arrow points to a specific state. Accept is boolean."""
        self.label = label
        self.arrows = arrows
        self.accept = accept

    def follows(self):
        states = {self}
        if self.label is None:
            for state in self.arrows:
                states = (states | state.follows())
        return states


class NFA:
    """Nondeterministic Finite Autamata."""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):  
        """Returns true if the NFA matches a string."""
        previous = self.start.follows()

        for c in s:
            current = set()
            for state in previous:
                if state.label == c:
                    current = (current | state.arrows[0].follows())
            previous = current
        return (self.end in previous)


# post fix notation to turn into a NFA
def re_to_nfa(postfix):
    # The stack for NFAs
    stack = []
    # Loop through the postfix
    for c in postfix:
        # Concatenation
        if c == '.':
            nfa2 = stack[-1] #pop top NFA from the stack
            stack = stack[:-1] # remove from stack
            nfa1 = stack[-1] # pop the next NFA from the stack
            stack = stack[:-1]
            nfa1.end.accept = False #accept state of nfa1 becomes non-acceot
            nfa1.end.arrows.append(nfa2.start) # point to start state of nfa2
            nfa = NFA(nfa1.start, nfa2.end) # make new nfa with nfa1's start state and nfa2's accept state.
            stack.append(nfa) # push to stack
        elif c == '|':  # OR logic character
            nfa2 = stack[-1]
            stack = stack[:-1]
            nfa1 = stack[-1]
            stack = stack[:-1]
            start = State(None, [], False)
            end = State(None, [], True)
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            nfa1.end.accept = False
            nfa2.end.accept = False
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            nfa = NFA(start, end)
            stack.append(nfa)
        elif c == '*':  #Kleene Star
            nfa1 = stack[-1]
            stack = stack[:-1]
            start = State(None, [], False)
            end = State(None, [], True)
            start.arrows.append(nfa1.start)
            start.arrows.append(end)
            nfa1.end.accept = False
            nfa1.end.arrows.append(end)
            nfa1.end.arrows.append(nfa1.start)
            nfa = NFA(start, end)
            stack.append(nfa)
        else: # non-special characters
            end = State(None, [], True)
            start = State(c, [], False)
            start.arrows.append(end)
            nfa = NFA(start, end)
            stack.append(nfa)

    if len(stack) != 1: #Should only have one NFA on the stack
        return None
    else:
        # returns the last nfa left on stack
        return stack[0]


if __name__ == "__main__":  
    for postfix in ["abb.*.a.", "100.*.1.", 'ab|']:
        print(f"postfix:   {postfix}")
        print(f"nfa: {re_to_nfa(postfix)}")
