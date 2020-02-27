# STATE: d -> (∅, ∅); k -> (∅, ∅); len(d) -> (∅, ∅); result -> (∅, ∅)
d: Dict[int, int] = {}

# STATE: d -> ({3}, ∅); k -> (∅, ∅); len(d) -> (∅, ∅); result -> (∅, ∅)
k: int = 3
# STATE: d -> ({k}, ∅); k -> (∅, ∅); len(d) -> (∅, ∅); result -> (∅, ∅)
result: int = d[k]
if result < 3:
    raise ValueError
