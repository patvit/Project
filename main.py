from statistics import mean


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades_bystydent:
                lecturer.grades_bystydent[course] += [grade]
            else:
                lecturer.grades_bystydent[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        num = 0
        count = 0
        for x in self.grades:
            num += sum(self.grades[x])
            count += len(self.grades[x])
        num = num / count
        res = f'Имя: {self.name} \nФамлиия: {self.surname}\nСредняя оценка за домашние задания:{num}\nКурсы в процессе изучения:{self.courses_in_progress}\nЗавершенные курсы:{self.finished_courses} '
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student')
            return
        return mean(self.grades['Python']) < mean(self.grades['Python'])

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    grades_bystydent = {
    }

    def __str__(self):
        num = mean(self.grades_bystydent['Python'])
        res = f'Имя: {self.name} \nФамлиия: {self.surname}\nСредняя оценка за лекции:{num}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
            return
        return mean(self.grades_bystydent['Python']) < mean(other.grades_bystydent['Python'])

class Reviewer (Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамлиия: {self.surname}'
        return res

def get_aver_grade_by_students(students, course):
    num = 0
    aver_num = 0
    for student in students:
        num += mean(student.grades[course])
    aver_num = num / len(students)
    print(f'средняя оценка студентов =', aver_num)

def get_aver_grade_by_lecturers(lecturers, course):
    num = 0
    aver_num = 0
    for lecturer in lecturers:
        num += mean(lecturer.grades_bystydent[course])
    aver_num = num / len(lecturers)
    print(f'средняя оценка лекторов =', aver_num)

#студент 1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']


#студент 2
best_student_second = Student('Silvestr', 'Stalone', 'your_gender')
best_student_second.courses_in_progress += ['Python']

#проверяющий 1
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['Git']



#проверяющий 2
cool_reviewer_second = Reviewer('Arnolnd', 'Shvarzneyger')
cool_reviewer_second.courses_attached += ['Python']

#лектор 1
cool_lecturer = Lecturer ('Ted', 'Baggy')
cool_lecturer.courses_attached += ['Python']

#лектор 2
cool_lecturer_second = Lecturer ('Bruce', 'Williace')
cool_lecturer_second.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Git', 5)


cool_reviewer.rate_hw(best_student_second, 'Python', 9)
cool_reviewer.rate_hw(best_student_second, 'Python', 9)
cool_reviewer.rate_hw(best_student_second, 'Python', 9)

print(best_student.name)

print(best_student.grades)
print(best_student.courses_in_progress)
print(best_student.finished_courses)


best_student.rate_lecturer_hw(cool_lecturer, 'Python', 10)
best_student.rate_lecturer_hw(cool_lecturer, 'Python', 10)

best_student.rate_lecturer_hw(cool_lecturer_second, 'Python', 8)
best_student.rate_lecturer_hw(cool_lecturer_second, 'Python', 8)

print(cool_lecturer.grades_bystydent)

print('some_reviewer')
print(cool_reviewer)

print('some_lecturer')
print(cool_lecturer)


print('some_student')
print(best_student)
print(best_student_second)

print('сравнение студентов')
print(best_student.__lt__(best_student_second))

print('сравнение лекторов')
print(cool_lecturer.__lt__(cool_lecturer_second))

print('средняя оценка студентов')
get_aver_grade_by_students([best_student, best_student_second], 'Python')

print('средняя оценка лекторов')
get_aver_grade_by_lecturers([cool_lecturer, cool_lecturer_second], 'Python')