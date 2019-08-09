
from typing import Dict, Tuple, IO

def f(N: int, Ms: Dict[(Tuple[(complex, complex)], str)]) -> Tuple[(complex, Dict[(Tuple[(complex, complex)], str)])]:
    star: Tuple[(complex, complex)] = (1, 1)
    changed: Dict[(Tuple[(complex, complex)], str)] = {
        
    }
    for i in range(1, (N + 1)):
        if ((1, i) in Ms):
            if (Ms[(1, i)] == 'x'):
                star: Tuple[(complex, complex)] = (1, i)
            elif (Ms[(1, i)] == 'o'):
                star: Tuple[(complex, complex)] = (1, i)
    if ((star not in Ms) or (Ms[star] != 'o')):
        changed[star]: str = 'o'
    for i in range(1, (N + 1)):
        if (((1, i) not in Ms) and (star != (1, i))):
            changed[(1, i)]: str = '+'
    for i in range(2, N):
        if ((N, i) not in Ms):
            changed[(N, i)]: str = '+'
    if (star == (1, 1)):
        for i in range(2, (N + 1)):
            if ((i, i) not in Ms):
                changed[(i, i)]: str = 'x'
    elif (star == (1, N)):
        for i in range(1, (N + 1)):
            if ((i, ((N + 1) - i)) not in Ms):
                changed[(i, ((N + 1) - i))]: str = 'x'
    else:
        for i in range(1, (N + 1)):
            p: Tuple[(complex, complex)] = (i, (((((star[1] - 1) + i) - 1) % N) + 1))
            if ((star[1] == 2) and ((N % 2) == 0)):
                p: Tuple[(complex, complex)] = (p[0], (((star[1] - i) % N) + 1))
            if ((p not in Ms) and (p != star) and (p not in changed)):
                changed[p]: str = 'x'
            if (i == N):
                star2: Tuple[(complex, complex)] = p
                if (N != 1):
                    changed[star2]: str = 'o'
    score: complex = 0
    sb: Dict[(str, complex)] = {
        '+': 1,
        'x': 1,
        'o': 2,
    }
    for i in range(1, (N + 1)):
        for j in range(1, (N + 1)):
            if ((i, j) in changed):
                score += sb[changed[(i, j)]]
            elif ((i, j) in Ms):
                score += sb[Ms[(i, j)]]
    return (score, changed)
fin: IO = open('d1.in')
fout: IO = open('d1.out', 'w')
T: int = int(fin.readline())
for t in range(1, (T + 1)):
    (N, M) = [int(x) for x in fin.readline().split(' ')]
    Ms: Dict[(Tuple[(complex, complex)], str)] = {
        
    }
    for _ in range(M):
        (v, i, j) = fin.readline().split(' ')
        i: float = int(i)
        j: float = int(j)
        Ms[(i, j)]: str = v
    (score, changed) = f(N, Ms)
    fout.write(('Case #%s: %s %s\n' % (t, score, len(changed))))
    for (i, j) in changed:
        fout.write(('%s %s %s\n' % (changed[(i, j)], i, j)))
    for i in range(1, (N + 1)):
        s: str = ''
        for j in range(1, (N + 1)):
            if ((i, j) in changed):
                s += changed[(i, j)]
            elif ((i, j) in Ms):
                s += Ms[(i, j)]
            else:
                s += '.'
