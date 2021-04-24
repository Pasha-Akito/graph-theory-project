# Thompson's construction

class State():
    """A State and its arrows in Thompson's construction."""

    # Constructor
    def __init__(self, label, arrows, accept):
        """Label is the arrow labels, arrows is a list os states to point to. accept is a boolean as to wheather this is an accept state."""
        self.label = label
        self.arrows = arrows
        self.accept = accept

    def followes(self):
        """The set of states that are gotten from following this state and all its e arrows."""
        # include this state in the returned set.
        states = {self}
        # If this state has e arrows, i.e. label is none.
        if self.label is None:
            # Loop through this state's arrows.
            for state in self.arrows:
                # Incorporate that state's earrow states in states.
                states = (states | state.followes())
        # Returns the set of states.
        return states


class NFA:
    """A non-deterministic finite automaton."""

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def match(self, s):  # self is first arg
        """Return True if this NFA (instance) matchess the string s."""
        previous = self.start.followes()

        for c in s:
            current = set()
            for state in previous:
                if state.label == c:
                    current = (current | state.arrows[0].followes())
            previous = current
        return (self.end in previous)


# post fix notation to turn into a NFA
def re_to_nfa(postfix):
    # A stack for NFAS
    stack = []
    # Loop through the postfix r.e. left to right.
    for c in postfix:
        # Concatenation
        if c == '.':
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack. on the left
            nfa1 = stack[-1]
            stack = stack[:-1]
            nfa1.end.accept = False
            nfa1.end.arrows.append(nfa2.start)  # empty list to begin with
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '|':  # or character
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            # Remove from stack up to but not including last one, will be placed on the right
            stack = stack[:-1]
            # Pop the next NFA off stack. on the left
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create a new start and end state.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make a new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '*':  
            nfa1 = stack[-1]
            # Remove from stack up to but not inculding last one, will be placed on the right
            stack = stack[:-1]
            # Create a bew start and end state.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make a new start state point at old start states.
            start.arrows.append(nfa1.start)
            # And at the new end state.
            start.arrows.append(end)
            # Make old end state non-accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old accept state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        else:
            # Create an NFA for the non-special character c.
            # Create the end state.
            end = State(None, [], True)
            # Create the start state.
            start = State(c, [], False)
            # Point new start state at new end state.
            start.arrows.append(end)
            # Create the NFA with the start and end state.
            nfa = NFA(start, end)
            # Append the NFA to the NFA stack.
            stack.append(nfa)

    # There should only be one NFA on the stack.
    if len(stack) != 1:
        return None  # error occured
    else:
        # returns nfa that was left on the stack after thompson runs once
        return stack[0]


if __name__ == "__main__":  
    for postfix in ["abb.*.a.", "100.*.1.", 'ab|']:
        print(f"postfix:   {postfix}")
        print(f"nfa: {re_to_nfa(postfix)}")
        print()
