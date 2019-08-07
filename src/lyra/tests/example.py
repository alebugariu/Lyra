grade2gpa: Dict[str, float] = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

file: List[str] = input()
for line in file:
    data: List[str] = line.split()
    grades: int = int(data[1])
    gpa: float = 0.0
    for i in range(2, grades + 2):
        gpa += grade2gpa[data[i]]
    result: float = gpa/grades
    print(data[0])
    print(result)

for letter_grade, numeric_grade in grade2gpa.items():
    print(letter_grade)
    print(numeric_grade)

if 'A' not in grade2gpa.keys():
    raise ValueError
if '4.0' not in grade2gpa.values():
    raise ValueError

if 'G' in grade2gpa.keys():
    raise ValueError
if '-1.0' in grade2gpa.values():
    raise ValueError

students2grades: Dict[int, List[float]] = dict()
number_of_students: int = input()
for student in range(number_of_students):
    number_of_grades: int = input()
    grades: List[float] = list()
    for grade_counter in range(number_of_grades):
        grade: float = input()
        grades.add(grade)
    students2grades[student] = grades

