class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_avg = 0

    def set_grade (self, lecturer, course_lect, grade_lect):
        if isinstance(lecturer, Lecturer) and course_lect in lecturer.courses_attached and course_lect in self.courses_in_progress:
            if course_lect in lecturer.course_grade:
                lecturer.course_grade[course_lect] += [grade_lect]
            else:
                lecturer.course_grade[course_lect] = [grade_lect]

    def get_avg_hw_score(self, grades):
        score = 0
        cnt = 0
        for itm in grades.values():
            cnt += len(itm)
            for scr in itm:
                score += scr
        self.grade_avg = score / cnt
        return self.grade_avg

    def __str__(self):
        self.get_avg_hw_score(self.grades)
        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за домашние задания: {self.grade_avg}, '\
              f'Курсы в процессе изучения: {self.courses_in_progress[0]}, '\
              f'Завершенные курсы: {self.finished_courses[0]}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.grade_avg < other.grade_avg

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.course_grade = {}
        self.course_grade_avg = 0

    def get_course_grade_avg (self, course_grade):
        score = 0
        cnt = 0
        for itm in course_grade.values():
            cnt += len(itm)
            for scr in itm:
                score += scr
        self.course_grade_avg = score / cnt
        return self.course_grade_avg

    def __str__(self):
        self.get_course_grade_avg(self.course_grade)
        res = f'Имя: {self.name}, Фамилия: {self.surname}, Средняя оценка за лекции: {self.course_grade_avg}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.course_grade_avg < other.course_grade_avg

class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}, ' \
              f'Фамилия: {self.surname}'
        return res


jane = Student('Jane', 'Ostin', 'female')
jane.courses_in_progress.append('Python')
jane.courses_in_progress.append('Git')
jane.finished_courses.append('Введение в программирование')

jake = Student('Jake', 'The Sparrow', 'male')
jake.courses_in_progress.append('Python')
jake.courses_in_progress.append('Git')
jake.finished_courses.append('Введение в программирование')

mr_white = Reviewer('Kyle','White')
mr_white.courses_attached.append('Python')
mr_white.courses_attached.append('Git')

mr_orange = Reviewer('Lewis', 'Orange')
mr_orange.courses_attached.append('Python')
mr_orange.courses_attached.append('Git')

mr_brown = Mentor('John', 'Brown')
mr_brown.courses_attached.append('Python')

mr_green = Lecturer('Jack', 'Green')
mr_green.courses_attached.append('Python')
mr_green.courses_attached.append('Git')

mr_blue = Lecturer('Jim', 'Blue')
mr_blue.courses_attached.append('Python')
mr_blue.courses_attached.append('Git')

jane.set_grade(mr_green,'Python', 9)
jane.set_grade(mr_green,'Python', 10)
jane.set_grade(mr_green,'Git', 9)

jake.set_grade(mr_green,'Python', 10)
jake.set_grade(mr_green,'Python', 9)
jake.set_grade(mr_green,'Git', 7)

jane.set_grade(mr_blue,'Python', 7)
jane.set_grade(mr_blue,'Python', 8)
jane.set_grade(mr_blue,'Git', 10)

jake.set_grade(mr_blue,'Python', 9)
jake.set_grade(mr_blue,'Python', 6)
jake.set_grade(mr_blue,'Git', 10)

mr_white.rate_hw(jake,'Python', 8)
mr_white.rate_hw(jake,'Git', 9)
mr_white.rate_hw(jake,'Python', 7)

mr_white.rate_hw(jane,'Python', 10)
mr_white.rate_hw(jane,'Git', 8)
mr_white.rate_hw(jane,'Python', 8)

mr_orange.rate_hw(jake,'Git', 9)
mr_orange.rate_hw(jake,'Git', 9)
mr_orange.rate_hw(jake,'Python', 10)

mr_orange.rate_hw(jane,'Git', 10)
mr_orange.rate_hw(jane,'Git', 9)
mr_orange.rate_hw(jane,'Python', 8)


print(jane)

print(jake)

print(mr_white)

print(mr_orange)

print(mr_green)

print(mr_blue)

print(jane > jake)

print(mr_green < mr_blue)