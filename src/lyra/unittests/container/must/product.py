def cartesian_product(inputs: List[List[str]]) -> List[List[str]]:
    solutions: int = 1
    for an_input in inputs:
        solutions *= len(an_input)

    product: List[List[str]] = list()
    for i in range(solutions):
        j: int = 1
        result_line: str = ''
        for input_line in inputs:
            result_line += input_line[(i/j) % len(input_line)]
            j *= len(input_line)
        product.append([result_line])
    return product


x: List[List[str]] = []
attempts: List[List[str]] = cartesian_product(x)
for attempt in attempts:
    # a -> (∅, ∅); attempt -> (∅, ∅); attempts -> (∅, ∅); b -> (∅, ∅); i -> (∅, ∅); len(a) -> (∅, ∅); len(attempt) -> (∅, ∅); len(attempts) -> (∅, ∅); len(b) -> (∅, ∅); len(x) -> (∅, ∅); x -> (∅, ∅)
    for i in range(10):
        a: Tuple[(int, int)] = (i, i)
        # a -> (∅, ∅); attempt -> ({i}, ∅); attempts -> (∅, ∅); b -> (∅, ∅); i -> (∅, ∅); len(a) -> (∅, ∅); len(attempt) -> (∅, ∅); len(attempts) -> (∅, ∅); len(b) -> (∅, ∅); len(x) -> (∅, ∅); x -> (∅, ∅)
        b: str = attempt[i]
        print(b)
