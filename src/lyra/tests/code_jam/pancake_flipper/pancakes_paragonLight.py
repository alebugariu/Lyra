def checkOnes(l: Dict[(int, int)]) -> int:
    ones: int = 0
    last: int = (- 1)
    for i in range(len(l)):
        if (i > 0):
            last: int = l[(i - 1)]
        if (l[i] == 0):
            if (last == 1):
                ones += 1
            else:
                continue
        elif (last == 1):
            continue
        else:
            continue
    return ones
if (__name__ == '__main__'):
    inputFile: str = 'inputQ1'
    inputFile: str = 'A-small-attempt3.in'
    outputFile: str = 'outputQ1'
    with open(inputFile) as in_file, open(outputFile, 'w') as out_file:
        cases: str = in_file.readline().strip()
        print(cases)
        for index in range(1, (int(cases) + 1)):
            rowData: None = in_file.readline().strip
            strs: List[str] = rowData.split(' ')
            k: int = int(strs[1])
            L: int = len(strs[0])
            F: List[str] = (['+'] * L)
            strF: str = ''.join(F)
            flag: bool = True
            old: str = strs[0]
            List: List[str] = []
            if (old == strF):
                flag: bool = False
            List.append(old)
            step: int = 0
            visited: Dict[(str, int)] = {
                
            }
            visited[old]: int = 1
            while flag:
                flag1: bool = True
                newList: List[str] = []
                for oldE in List:
                    for i in range(((L - k) + 1)):
                        new: str = oldE
                        newS: List[str] = list(new)
                        for j in range(i, (i + k)):
                            if (newS[j] == '+'):
                                newS[j]: str = '-'
                            else:
                                newS[j]: str = '+'
                        new: str = ''.join(newS)
                        if (index == 10):
                            print(new)
                        if (new == strF):
                            flag1: bool = False
                            flag: bool = False
                            break
                        elif (new not in visited):
                            newList.append(new)
                            visited[new]: int = 1
                            flag1: bool = False
                if flag1:
                    flag: bool = False
                    step: int = (- 1)
                else:
                    step += 1
                    del List[:]
                    List: List[str] = newList[:]
            o: str = str(step)
            if (step == (- 1)):
                o: str = 'IMPOSSIBLE'
            outputString: str = (((('Case #' + str(index)) + ': ') + o) + '\n')
            out_file.write(outputString)
