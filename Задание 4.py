class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def average_grade(self):
        return round(sum(self.grades.values()) / len(self.grades), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lectures_given = 0

    def give_lecture(self, course):
        self.lectures_given += 1

    def average_grade(self):
        return round(sum(self.grades) / len(self.grades), 1)

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}"

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def calculate_average_homework_grade(students, course_name):
    total_grade = 0
    for student in students:
        if course_name in student.grades:
            total_grade += sum(student.grades[course_name])
    return round(total_grade / len(students), 1)

def calculate_average_lecture_grade(lecturers, course_name):
    total_grade = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            total_grade += sum(lecturer.grades[course_name])
    return round(total_grade / len(lecturers), 1)

best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_in_progress += ['Python']

some_reviewer = Reviewer("Some", "Buddy")

best_student.average_grade()
cool_mentor.average_grade()
some_lecturer.average_grade()
some_reviewer.average_grade()

print(calculate_average_homework_grade([best_student], 'Python'))
print(calculate_average_lecture_grade([some_lecturer], 'Python'))