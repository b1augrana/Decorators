import os
from datetime import datetime
from logger_par import logger_par


path = 'main.log'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
 
    @logger_par(path)
    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'
        
        
    def _mid_grade(self):
        mid_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)  
            mid_sum += course_mid  
        if mid_sum == 0:
            return f'Оценок пока нет'        
        else:
            return f'{mid_sum / len(self.grades.values()):.2f}'
        
     
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        res += f'Средняя оценка за домашние задания: {self._mid_grade()} \n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res 
    
    
    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Не является студентом.')
            return
        return self._mid_grade() < student._mid_grade()
    
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}
        
        
class Lecturer(Mentor):
    def _mid_rate(self):
        mid_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            course_mid = course_sum / len(course_grades)
            mid_sum += course_mid
        if mid_sum == 0:
            return f'Оценок пока нет'
        else:
            return f'{mid_sum / len(self.rates.values()):.2f}'
        

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка {self._mid_rate()}\n'
        return res
    

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f'Не является лектором')
            return
        return self._mid_rate() < lecturer._mid_rate()

    
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
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'    
        return res
    
    
def students_average_grade(students, course):
    mid_sum_grades = 0
    counter = 0
    for st in students:
        if course in st.grades.keys():
            st_sum_grades = 0
            for grade in st.grades[course]:
                st_sum_grades += grade
            mid_st_sum_grades = st_sum_grades / len(st.grades[course])    
            mid_sum_grades += mid_st_sum_grades
            counter += 1
    if mid_sum_grades == 0:
        return f'Нет оценок по данному предмету.'
    else:
        return f'{mid_sum_grades / counter:.2f}' 
        
        
def lecturers_average_rate(lecturers, course):
    mid_sum_rates = 0
    counter = 0
    for lect in lecturers:
        if course in lect.rates.keys():
            lect_sum_rates = 0
            for rate in lect.rates[course]:
                lect_sum_rates += rate
            mid_lect_sum_rates = lect_sum_rates / len(lect.rates[course])    
            mid_sum_rates += mid_lect_sum_rates
            counter += 1
    if mid_sum_rates == 0:
        return f'Нет оценок по данному предмету.'
    else:
        return f'{mid_sum_rates / counter:.2f}' 
        
   
 
student1 = Student('Ruoy', 'Eman', 'male')
student1.finished_courses = ['English']
student1.courses_in_progress = ['Python', 'Git']
 
student2 = Student('Helen', 'Hunter', 'female') 
student2.finished_courses = ['Data Science']
student2.courses_in_progress = ['Python', 'Git']

students = [student1, student2]

lecturer1 = Lecturer('Some', 'Buddy') 
lecturer1.courses_attached = ['Python']

lecturer2 = Lecturer('Guy', 'Man')
lecturer2.courses_attached = ['Python', 'Git']

lecturers = [lecturer1, lecturer2]

reviewer1 = Reviewer('Todd', 'Howard')
reviewer1.courses_attached = ['English', 'Git', 'Python']

reviewer2 = Reviewer('Mira', 'Ivanova')
reviewer2.courses_attached = ['Git', 'Python', 'Data Science']

 
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'English', 8)
reviewer1.rate_hw(student1, 'English', 8)
reviewer1.rate_hw(student1, 'English', 9)
reviewer1.rate_hw(student2, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 9)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Git', 10)
reviewer1.rate_hw(student2, 'Git', 8)
reviewer1.rate_hw(student2, 'Git', 10)

reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Python', 9)
reviewer2.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student1, 'Git', 10)
reviewer2.rate_hw(student1, 'Git', 9)
reviewer2.rate_hw(student2, 'Python', 10)
reviewer2.rate_hw(student2, 'Python', 7)
reviewer2.rate_hw(student2, 'Python', 9)
reviewer2.rate_hw(student2, 'Data Science', 9)
reviewer2.rate_hw(student2, 'Data Science', 7)
reviewer2.rate_hw(student2, 'Data Science', 8)

student1.rate_lecturer(lecturer1, 'Python', 10) 
student1.rate_lecturer(lecturer1, 'Python', 10) 
student1.rate_lecturer(lecturer1, 'Python', 10) 
student1.rate_lecturer(lecturer2, 'Python', 9) 
student1.rate_lecturer(lecturer2, 'Python', 10) 
student1.rate_lecturer(lecturer2, 'Python', 9) 

student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 9)
student2.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)
student1.rate_lecturer(lecturer2, 'Git', 9)
student1.rate_lecturer(lecturer2, 'Git', 8)
student1.rate_lecturer(lecturer2, 'Git', 7)
student2.rate_lecturer(lecturer2, 'Git', 6)
student2.rate_lecturer(lecturer2, 'Git', 9)
student2.rate_lecturer(lecturer2, 'Git', 8)


print(student1)
print()
print(student2)


if student1 > student2:
    print(f'Средний балл у {student1.name} {student1.surname} выше, чем у {student2.name} {student2.surname}')
else:
    print(f'Средний балл у {student2.name} {student2.surname} выше, чем у {student1.name} {student1.surname}')    
    
print(reviewer1)    
print(reviewer2)

print(lecturer1)
print(lecturer2)

if lecturer1 > lecturer2:
    print(f'Средний балл у {lecturer1.name} {lecturer1.surname} выше, чем у {lecturer2.name} {lecturer2.surname}')
else:
    print(f'Средний балл у {lecturer2.name} {lecturer2.surname} выше, чем у {lecturer1.name} {lecturer1.surname}')    
    
print(f'Средний балл студентов по курсу "Python": {students_average_grade(students, "Python")}')    
print(f'Средний балл студентов по курсу "Git": {students_average_grade(students, "Git")}')       

print(f'Средний балл лекторов по курсу "Python": {lecturers_average_rate(lecturers, "Python")}')    
print(f'Средний балл лекторов по курсу "Git": {lecturers_average_rate(lecturers, "Git")}')  