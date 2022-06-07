from oop.person_motivating_task import is_person_using_gmail


class Person:

    def __init__(self, first_name, last_name, city, address, phone, email, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.address = address
        self.phone = phone
        self.email = email
        self.age = age
        self.new_att = None

    def is_using_gmail(self):
        return self.email.endswith("@gmail.com")


if __name__ == '__main__':
    person1 = Person('Moshe', 'Israeli', 'Tel-Aviv', 'Rotshild 45', '0545555555', 'moshe@gmail.com', 28)
    person2 = Person('David', 'Erel', 'Herzliya', 'Hertzl 3', '05523647234', 'david@protonmail.com')

    # person1.first_name = 'Oren'
    #
    # print(f"person 1 last name: {person1.last_name}")
    # print(f"person 2 last name: {person2.last_name}")
    #
    # print(f"person 1 first name: {person1.first_name}")

    # person1_dict = {
    #     'first_name': 'Moshe',
    #     'last_name': 'Israeli',
    #     'city': 'Tel-Aviv',
    #     'address': 'Rotshild 45',
    #     'phone': '0545555555',
    #     'email': 'moshe@gmail.com',
    #     'age': 28
    # }
    # is_person_using_gmail(person1_dict)

    print(person1.is_using_gmail())
    print(person2.is_using_gmail())
    # Person.is_using_gmail(person1)

    person1.new_att = 67



