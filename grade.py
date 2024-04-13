class Student:
    def __init__(self, id, name, english_score, c_score, python_score):
        self.id = id
        self.name = name
        self.scores = [english_score, c_score, python_score]
        self.total = sum(self.scores)
        self.average = self.total / len(self.scores)
        self.grade = self.calculate_grade()
        self.rank = 0

    def calculate_grade(self):
        if self.average >= 90: return 'A'
        elif self.average >= 80: return 'B'
        elif self.average >= 70: return 'C'
        elif self.average >= 60: return 'D'
        else: return 'F'

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, English Score: {self.scores[0]}, C Score: {self.scores[1]}, Python Score: {self.scores[2]}, Total: {self.total}, Average: {self.average:.2f}, Grade: {self.grade}, Rank: {self.rank}"

def input_student():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    english_score = int(input("Enter English Score: "))
    c_score = int(input("Enter C Score: "))
    python_score = int(input("Enter Python Score: "))
    return Student(id, name, english_score, c_score, python_score)

def calculate_rank(students):
    for i in range(len(students)):
        students[i].rank = sum(s.total > students[i].total for s in students) + 1

students = [input_student() for _ in range(5)]
calculate_rank(students)
for student in students:
    print(student)