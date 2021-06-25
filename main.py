class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


jane = Student('Jane', 'Ostin', 'female')
mr_smith = Mentor('Kyle','Smith')
jane.finished_courses.append('physics')
jane.finished_courses.append('math')
jane.grades[jane.finished_courses[0]] = 'A'
jane.grades[jane.finished_courses[1]] = 'A+'
print(jane.__dict__)


print(jane.name, jane.surname, jane.gender, jane.grades)
print(mr_smith.name, mr_smith.surname)
