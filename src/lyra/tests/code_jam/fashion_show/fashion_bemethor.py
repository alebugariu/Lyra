
from typing import List

def score(l: List[List[object]], n: int) -> int:
    s: int = 0
    for i in range(n):
        for j in range(n):
            if (l[i][j] == 'o'):
                s += 2
            if ((l[i][j] == '+') or (l[i][j] == 'x')):
                s += 1
    return s
t: int = int(input())
for t_index in range(t):
    (n, m) = input().split()
    n: int = int(n)
    m: int = int(m)
    l: List[List[object]] = []
    l_beg: List[List[object]] = []
    for _ in range(n):
        l.append([])
        l_beg.append([])
        for _ in range(n):
            l[(- 1)].append('')
            l_beg[(- 1)].append('')
    for _ in range(m):
        (c, i, j) = input().split()
        i: int = (int(i) - 1)
        j: int = (int(j) - 1)
        l[i][j]: object = c
        l_beg[i][j]: object = c
    l0: List[object] = l[0]
    index: int = (- 1)
    if (l0.count('o') == 0):
        if (l0.count('x') == 1):
            for i in range(n):
                if (l0[i] == 'x'):
                    l0[i]: object = 'o'
                    index: int = i
                if (l0[i] == ''):
                    l0[i]: object = '+'
        else:
            p: complex = False
            for i in range(n):
                if (l0[i] == ''):
                    if (not p):
                        l0[i]: object = 'o'
                        index: int = i
                        p: complex = True
                    else:
                        l0[i]: object = '+'
            if (not p):
                l0[0]: object = 'o'
                index: int = 0
    else:
        for i in range(n):
            if (l0[i] == ''):
                l0[i]: object = '+'
            if (l0[i] == 'o'):
                index: int = i
    i: int = 0
    if (index != (n - 1)):
        for j in range(1, n):
            if (i == index):
                i += 1
            l[j][i]: object = 'x'
            i += 1
    else:
        for j in range(1, n):
            l[j][((n - 1) - j)]: object = 'x'
            i += 1
    ln: List[object] = l[(- 1)]
    for i in range(1, (n - 1)):
        ln[i]: object = '+'
    s: complex = score(l, n)
    changes: List[None] = []
    for i in range(n):
        for j in range(n):
            if (l[i][j] != l_beg[i][j]):
                changes.append((l[i][j], (i + 1), (j + 1)))
    print(((((('Case #' + str((t_index + 1))) + ': ') + str(s)) + ' ') + str(len(changes))))
    for r in changes:
        print(((((r[0] + ' ') + str(r[1])) + ' ') + str(r[2])))
