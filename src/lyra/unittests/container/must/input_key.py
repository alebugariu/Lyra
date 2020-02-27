# STATE: d -> (∅, ∅); k -> (∅, ∅); len(d) -> (∅, ∅); result -> (∅, ∅)
d: Dict[int, int] = input()

# STATE: d -> (∅, ∅); k -> (∅, ∅); len(d) -> (∅, ∅); result -> (∅, ∅)
k: int = int(input())
# STATE: d -> ({k}, ∅); k -> (∅, ∅); len(d) -> (∅, ∅); result -> (∅, ∅)
result: int = d[k]
if result < 3:
    raise ValueError
