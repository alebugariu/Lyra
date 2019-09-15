d: Dict[int, int] = input()

k: int = 3
result: int = d[k]
if result < 3:
    raise ValueError
