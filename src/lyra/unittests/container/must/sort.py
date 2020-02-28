def sort(queue: List[str], table: Dict[(str, int)]):
    elements: int = len(queue)
    for i in range(elements-1):
        for j in range(i+1, elements):
            index_i: int = table[queue[i]]
            index_j: int = table[queue[j]]
            if index_i > index_j:
                aux: str = queue[i]
                queue[i] = queue[j]
                queue[j] = aux

q: List[str] = []
t: Dict[(str, int)] = []
sort(q, t)
