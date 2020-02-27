def flips(sequence: str, k: int) -> int:
    count: int = 0
    reached: Set[str] = set()
    if done(sequence):
        return 0
    else:
        count: int = (count + 1)
        iterations: Set[str] = generate_flips(sequence, k, reached)
        while (len(iterations) > 0):
            new_iterations: Set[str] = set()
            for item in iterations:
                if done(item):
                    return count
                else:
                    reached.add(item)
                    new_iteration: str = generate_flips(item, k, reached)
                    new_iterations.update(new_iteration)
            iterations: Set[str] = new_iterations
            count: int = (count + 1)
        return (- 1)


def done(sequence: str) -> bool:
    ele: str = ''
    for ele in sequence:
        if (ele == '-'):
            return False
    return True


def generate_flips(sequence: str, k: int, reached: Set[str]) -> Set[str]:
    new_iterations: Set[str] = set()
    for i in range(0, ((len(sequence) + 1) - k)):
        flipped_string: str = flip(sequence[i:(i + k)])
        new_string: str = sequence[:i] + flipped_string + sequence[(i + k):]
        if (new_string not in reached):
            new_iterations.add(new_string)
            reached.add(new_string)
    return new_iterations


def flip(string: str) -> str:
    new_string: str = ''
    i: str = ''
    for i in string:
        if (i == '+'):
            new_string: str = (new_string + '-')
        else:
            new_string: str = (new_string + '+')
    return new_string


data: str = input()
all_inputs: List[str] = data.split()
inputs: List[str] = all_inputs[1:]
answer: str = ''
count: int = 1
for line in inputs:
    split_line: List[str] = line.split()
    sequence: str = split_line[0]
    k: str = split_line[1]
    line_answer: int = flips(sequence, int(k))
    if (line_answer == (- 1)):
        answer: str = (((answer + 'Case #') + str(count)) + ': IMPOSSIBLE\n')
    else:
        answer: str = (((((answer + 'Case #') + str(count)) + ': ') + str(line_answer)) + '\n')
    count: int = (count + 1)
print(answer)
