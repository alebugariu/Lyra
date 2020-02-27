# STATE: len(r) -> (∅, ∅); len(x) -> (∅, ∅); r -> (∅, ∅); x -> (∅, ∅)
x: List[Tuple[(str, int, int)]] = []
for r in x:
    # STATE: len(r) -> (∅, ∅); len(x) -> (∅, ∅); r -> ({0, 1, 2}, ∅); x -> (∅, ∅)
    print(str(r[0]) + ' ' + str(r[1]) + ' ' + str(r[2]))
