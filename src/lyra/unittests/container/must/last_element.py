# STATE: l -> (∅, ∅); len(l) -> (∅, ∅)
l: List[int] = input()

# STATE: l -> ({0, len(l) + (-1)}, ∅); len(l) -> (∅, ∅)
if l[0] == 3:
    raise ValueError

# STATE: l -> ({len(l) + (-1)}, {3}); len(l) -> (∅, ∅)
if l[-1] != 3:
    raise ValueError
