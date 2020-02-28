def test_list():
    x: List[List[str]] = []
    for i in range(10):
        x[i] = ['test']
    return x

# STATE: l -> (∅, ∅); len(l) -> (∅, ∅); len(line) -> (∅, ∅); line -> (∅, ∅)
l: List[List[str]] = test_list()

# STATE: l -> (∅, ∅); len(l) -> (∅, ∅); len(line) -> (∅, ∅); line -> (∅, ∅)
for line in l:
    # STATE: l -> (∅, ∅); len(l) -> (∅, ∅); len(line) -> (∅, ∅); line -> (∅, ∅)
    print(line)
