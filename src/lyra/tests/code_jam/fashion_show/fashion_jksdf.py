
from typing import Set, List, Sequence, Tuple

def printout(n: complex, v: Sequence) -> None:
    print(((('Case #' + str(n)) + ': ') + str(v)))

def isCorrect(arr: complex) -> None:
    symbols: Set[None] = set()
    for (i, j) in enumerate(arr):
        for (k, l) in enumerate(j):
            if (l != '.'):
                symbols.add((l, i, k))
    for i in symbols:
        for j in symbols:
            if (i != j):
                if ((i[1] == j[1]) or (i[2] == j[2])):
                    if ((i[0] == '+') or (j[0] == '+')):
                        pass
                    else:
                        print('ZLEEEE')
                if (((i[1] + i[2]) == (j[1] + j[2])) or ((i[1] - i[2]) == (j[1] - j[2]))):
                    if ((i[0] == 'x') or (j[0] == 'x')):
                        pass
                    else:
                        print('ZLEEEE2')

def call(ii: float) -> None:
    (n, m) = [int(i) for i in input().split()]
    row: List[str] = [' ' for i in range(n)]
    nonplus: int = (- 1)
    for i in range(m):
        (v, r, c) = input().split()
        row[(int(c) - 1)]: str = v
        if (v != '+'):
            nonplus: int = (int(c) - 1)
    res: List[Tuple[(Sequence, float, float)]] = []
    if (nonplus == (- 1)):
        nonplus: int = 0
        row[0]: str = 'o'
        res.append(('o', 0, 0))
    for (i, v) in enumerate(row):
        if (v == ' '):
            res.append(('+', 0, i))
        elif (v == 'x'):
            res.append(('o', 0, i))
            nonplus: int = i
    for i in range(0, nonplus):
        res.append(('x', (i + 1), i))
    for i in range((nonplus + 1), n):
        res.append(('x', i, i))
    for i in range(1, (n - 1)):
        res.append(('+', (n - 1), i))
        "\n  #print n, row\n  s=[['.' for j in range(n)] for i in range(n)]\n  s[0] = row\n  for i in res:\n    s[i[1]][i[2]] = i[0]\n  st=''\n  for i in s:\n    for j in i:\n      st+=j\n    st+='\n'\n  #print st\n  \n  return"
    printout(ii, ((str((((3 * n) - 2) if (n != 1) else 2)) + ' ') + str(len(res))))
    for i in res:
        print(i[0], (i[1] + 1), (i[2] + 1))
t: int = int(input())
for ii in range(t):
    call((ii + 1))
