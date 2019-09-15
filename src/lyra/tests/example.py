grade2gpa: Dict[str, float] = input()

number_of_students: int = int(input())
for line_number in range(number_of_students):
    line: str = input()
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

students2grades: Dict[int, List[float]] = input()
for student in range(number_of_students):
    grades_for_student: List[float] = students2grades[student]
    print(grades_for_student)
