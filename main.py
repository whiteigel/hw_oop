class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.grade_avg = 0

    # students can grade lecturers for lectures

    def set_grade (self, lecturer, course_lect, grade_lect):
        if isinstance(lecturer, Lecturer) and course_lect in lecturer.courses_attached and course_lect in self.courses_in_progress:
            if course_lect in lecturer.course_grade:
                lecturer.course_grade[course_lect] += [grade_lect]
            else:
                lecturer.course_grade[course_lect] = [grade_lect]

    # getting average score for student's homework

    def get_avg_hw_score(self, grades):
        score = 0
        cnt = 0
        for itm in grades.values():
            cnt += len(itm)
            for scr in itm:
                score += scr
        self.grade_avg = score / cnt
        return self.grade_avg

    def course_list_to_string(self, course_list):
        lst = course_list
        separator = ', '
        return separator.join(lst)

    # redifining student's __str__

    def __str__(self):
        course_in_progress_list = self.course_list_to_string(self.courses_in_progress)
        finished_cources_list = self.course_list_to_string(self.finished_courses)
        avg_hw_scr = self.get_avg_hw_score(self.grades)
        res = f'Имя: {self.name} \n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {round(avg_hw_scr, 2)}\n '\
              f'Курсы в процессе изучения: {course_in_progress_list}\n '\
              f'Завершенные курсы: {finished_cources_list}'
        return res

    # redifining student's __lt__

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
        super().__init__(name, surname)
        self.courses_attached = []
        self.course_grade = {}
        self.course_grade_avg = 0

    # getting average score for lecturer's work

    def get_course_grade_avg (self, course_grade):
        score = 0
        cnt = 0
        for itm in course_grade.values():
            cnt += len(itm)
            for scr in itm:
                score += scr
        self.course_grade_avg = score / cnt
        return self.course_grade_avg

    # redefining lecturers' __str__

    def __str__(self):
        avg_course_grade = self.get_course_grade_avg(self.course_grade)
        res = f'Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {round(avg_course_grade,2)}'
        return res

    # redefining lecturers' __lt__

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.course_grade_avg < other.course_grade_avg

class Reviewer(Mentor):

    # rating student's homeworks

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # redefining reviewer' __str__

    def __str__(self):
        res = f'Имя: {self.name}\n Фамилия: {self.surname}'
        return res

# populating environment with people and data

jane = Student('Jane', 'Ostin', 'female')
jane.courses_in_progress.append('Python')
jane.courses_in_progress.append('Git')
jane.finished_courses.append('Введение в программирование')

jake = Student('Jake', 'Smith', 'male')
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

mr_black = Mentor('Erwin', 'Black')
mr_black.courses_attached.append('Git')

mr_green = Lecturer('Jack', 'Green')
mr_green.courses_attached.append('Python')
mr_green.courses_attached.append('Git')

mr_blue = Lecturer('Jim', 'Blue')
mr_blue.courses_attached.append('Python')
mr_blue.courses_attached.append('Git')

jane.set_grade(mr_green,'Python', 9)
jane.set_grade(mr_green,'Python', 7)
jane.set_grade(mr_green,'Git', 9)

jake.set_grade(mr_green,'Python', 6)
jake.set_grade(mr_green,'Python', 7)
jake.set_grade(mr_green,'Git', 5)

jane.set_grade(mr_blue,'Python', 7)
jane.set_grade(mr_blue,'Python', 8)
jane.set_grade(mr_blue,'Git', 3)

jake.set_grade(mr_blue,'Python', 5)
jake.set_grade(mr_blue,'Python', 7)
jake.set_grade(mr_blue,'Git',3)

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

# average students' grade for homeworks

students = [jane, jake]
def students_grade_avg(students, course):
    res = 0
    cnt = 0
    for item in students:
        for grades in item.grades[course]:
            res += grades
            cnt += 1
    return f"Средняя оценка студентов на курсе {course} равна {res/cnt}"

# average lecturers' grade for work

lect_list = [mr_green, mr_blue]
def lecturer_grade_avg(lecturers, course):
    res = 0
    cnt = 0
    for item in lecturers:
        for grades in item.course_grade[course]:
            res += grades
            cnt += 1
    return f"Средняя оценка лекторов за курс {course} равна {res/cnt}"

# printing results

print()
print(f'Student:\n {jane}')
print()
print(f'Student: \n {jake}')
print()
print(f'Mentor:\n {mr_brown.name} {mr_brown.surname}')
print()
print(f'Mentor:\n {mr_black.name} {mr_black.surname}')
print()
print(f'Reviewer:\n {mr_white}')
print()
print(f'Reviewer:\n {mr_orange}')
print()
print(f'Lecturer:\n {mr_green}')
print()
print(f'Lecturer:\n {mr_blue}')
print()
print(f"Средняя оценка Джейн за домашние задания выше чем у Джейка -",jane > jake)
print()
print("Среднняя оценка за лекции, полученная мистером Грином, ниже чем оценка мистера Блу -",mr_green < mr_blue)
print()
print(students_grade_avg(students, 'Python'))
print()
print(lecturer_grade_avg(lect_list, 'Git'))