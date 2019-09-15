d: Dict[int, int] = input()

k: int = int(input())
result: int = d[k]
if result < 3:
    raise ValueError
