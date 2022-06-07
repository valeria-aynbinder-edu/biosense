from oop.person_motivating_task import is_person_using_gmail


class Person:

    def __init__(self, first_name, last_name, city, address, phone, email):
        print("__init__ in Person")
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.address = address
        self.phone = phone
        self.email = email

    def is_using_gmail(self):
        return self.email.endswith("@gmail.com")


class Student(Person):

    def __init__(self, first_name, last_name, city, address, phone, email):
        print("__init__ in Student")
        super().__init__(first_name, last_name, city, address, phone, email)

        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)


class Lecturer(Person):

    def __init__(self, first_name, last_name, city, address, phone, email, salary_per_course):
        print("__init__ in Lecturer")
        super().__init__(first_name, last_name, city, address, phone, email)

        self.salary = salary_per_course
        self.courses = []

    def add_course(self, name):
        self.courses.append(name)

    def calc_salary(self):
        return len(self.courses) * self.salary + 1000


class SeniorLecturer(Lecturer):

    def __init__(self, first_name, last_name, city, address, phone, email, salary):
        super().__init__(first_name, last_name, city, address, phone, email, salary)

        self.conferences = []

    def add_conference(self, conf_data):
        self.conferences.append(conf_data)

    def calc_salary(self):
        return super().calc_salary() + len(self.conferences) * self.salary * 1.5

if __name__ == '__main__':

    student = Student('Moshe', 'Israeli', 'Tel-Aviv', 'Rotshild 45', '0545555555', 'moshe@gmail.com')
    print(student.is_using_gmail())
    student.add_grade(90)

    person2 = Person('David', 'Erel', 'Herzliya', 'Hertzl 3', '05523647234', 'david@protonmail.com')

    lec = Lecturer('Valeria', 'Erel', 'Herzliya', 'Hertzl 3', '05523647234', 'david@protonmail.com', 100)
    lec.add_course("data science")
    lec.add_course("python")

    print(f"Salary of lecturer: {lec.calc_salary()}")

    senior = SeniorLecturer("Orit", "Blabla",  'Herzliya', 'Hertzl 3', '05523647234', 'david@protonmail.com', 200)
    #
    senior.add_course("python")
    senior.add_conference("conference DEvGeekWeek")
    #

    lecturers = [lec, senior]
    for i in lecturers:
        print(f"{i.last_name}: {i.calc_salary()}")

    print(f"Salary of senior: {senior.calc_salary()}")
    # print(f"Courses: {senior.courses}")
    # print(f"Conferences: {senior.conferences}")

    # l = [student, person2, lec]
    #
    # for per in l:
    #     print(per.first_name)




# if __name__ == '__main__':
#     person1 = Person('Moshe', 'Israeli', 'Tel-Aviv', 'Rotshild 45', '0545555555', 'moshe@gmail.com', 28)
#     person2 = Person('David', 'Erel', 'Herzliya', 'Hertzl 3', '05523647234', 'david@protonmail.com')
#
#     # person1.first_name = 'Oren'
#     #
#     # print(f"person 1 last name: {person1.last_name}")
#     # print(f"person 2 last name: {person2.last_name}")
#     #
#     # print(f"person 1 first name: {person1.first_name}")
#
#     # person1_dict = {
#     #     'first_name': 'Moshe',
#     #     'last_name': 'Israeli',
#     #     'city': 'Tel-Aviv',
#     #     'address': 'Rotshild 45',
#     #     'phone': '0545555555',
#     #     'email': 'moshe@gmail.com',
#     #     'age': 28
#     # }
#     # is_person_using_gmail(person1_dict)
#
#     print(person1.is_using_gmail())
#     print(person2.is_using_gmail())
#     # Person.is_using_gmail(person1)
#
#     person1.new_att = 67


