# STATE: l -> (∅, ∅); last -> (∅, ∅); len(l) -> (∅, ∅)
l: List[int] = input()

# STATE: l -> ({0, len(l) + (-1), len(l) + (-2)}, ∅); last -> (∅, ∅); len(l) -> (∅, ∅)
last: int = l[-1]

# STATE: l -> ({0, len(l) + (-2)}, ∅); last -> (∅, ∅); len(l) -> (∅, ∅)
if l[0] == 3:
    raise ValueError

# STATE: l -> ({len(l) + (-2)}, {3}); last -> (∅, ∅); len(l) -> (∅, ∅)
if l[-2] != 3:
    raise ValueError
