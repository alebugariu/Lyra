d: Dict[int, int] = input()

if 3 not in d.keys():
    raise ValueError
if 4 in d.keys():
    raise ValueError
