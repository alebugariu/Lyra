d: Dict[int, int] = input()

# STATE: d -> ({3}, ∅); len(d) -> (∅, ∅)
if 3 not in d.keys():
    raise ValueError
# STATE: d -> (∅, ∅); len(d) -> (∅, ∅)
if 4 in d.keys():
    raise ValueError
