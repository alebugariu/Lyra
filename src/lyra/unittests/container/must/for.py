# STATE: data -> (∅, ∅); gpa -> (∅, ∅); grade2gpa -> (∅, ∅); grades -> (∅, ∅); i -> (∅, ∅); len(data) -> (∅, ∅); len(grade2gpa) -> (∅, ∅); line_number -> (∅, ∅); number_of_students -> (∅, ∅); result -> (∅, ∅)
grade2gpa: Dict[str, float] = {'A': 4.0, 'B': 3.0, 'C': 2.0, 'D': 1.0, 'F': 0.0}

number_of_students: int = int(input())
for line_number in range(number_of_students):
    data: List[str] = input().split()
    # STATE: data -> ({0, 1}, ∅); gpa -> (∅, ∅); grade2gpa -> (∅, ∅); grades -> (∅, ∅); i -> (∅, ∅); len(data) -> (∅, ∅); len(grade2gpa) -> (∅, ∅); line_number -> (∅, ∅); number_of_students -> (∅, ∅); result -> (∅, ∅)
    grades: int = int(data[1])
    gpa: float = 0.0
    # STATE: data -> ({0}, ∅); gpa -> (∅, ∅); grade2gpa -> (∅, ∅); grades -> (∅, ∅); i -> (∅, ∅); len(data) -> (∅, ∅); len(grade2gpa) -> (∅, ∅); line_number -> (∅, ∅); number_of_students -> (∅, ∅); result -> (∅, ∅)
    for i in range(2, grades + 2):
        # STATE: data -> ({0}, ∅); gpa -> (∅, ∅); grade2gpa -> ({data[i]}, ∅); grades -> (∅, ∅); i -> (∅, ∅); len(data) -> (∅, ∅); len(grade2gpa) -> (∅, ∅); line_number -> (∅, ∅); number_of_students -> (∅, ∅); result -> (∅, ∅)
        gpa += grade2gpa[data[i]]
    result: float = gpa/grades
    # STATE: data -> ({0}, ∅); gpa -> (∅, ∅); grade2gpa -> (∅, ∅); grades -> (∅, ∅); i -> (∅, ∅); len(data) -> (∅, ∅); len(grade2gpa) -> (∅, ∅); line_number -> (∅, ∅); number_of_students -> (∅, ∅); result -> (∅, ∅)
    print(data[0])
    print(result)
