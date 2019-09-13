
from typing import List, Dict, Tuple
T: int = int(input().strip())
for t in range(1, (T + 1)):
    line: List[str] = input().strip().split(' ')
    R: int = int(line[0])
    C: int = int(line[1])
    grid: List[List[str]] = []
    inits: Dict[(str, Tuple[(int, int)])] = {
        
    }
    for r in range(R):
        grid.append(list(input().strip()))
        for c in range(C):
            if (grid[r][c] != '?'):
                inits[grid[r][c]]: Tuple[(int, int)] = (r, c)
    for i in inits:
        (ulr, ulc) = inits[i]
        (lrr, lrc) = inits[i]
        while ((ulc > 0) and (grid[ulr][(ulc - 1)] == '?')):
            ulc -= 1
        while ((lrc < (C - 1)) and (grid[lrr][(lrc + 1)] == '?')):
            lrc += 1
        while ((ulr > 0) and all([(x == '?') for x in grid[(ulr - 1)][ulc:(lrc + 1)]])):
            ulr -= 1
        while ((lrr < (R - 1)) and all([(x == '?') for x in grid[(lrr + 1)][ulc:(lrc + 1)]])):
            lrr += 1
        for r in range(ulr, (lrr + 1)):
            for c in range(ulc, (lrc + 1)):
                grid[r][c]: str = i
    print(('Case #%d:' % (t,)))
    for row in grid:
        print(''.join(row))
