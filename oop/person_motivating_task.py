## Motivating task

person1 = {
    'first_name': 'Moshe',
    'last_name': 'Israeli',
    'city': 'Tel-Aviv',
    'address': 'Rotshild 45',
    'phone': '0545555555',
    'email': 'moshe@gmail.com',
    'age': 28
}

person2 = {
    'first_name': 'David',
    'last_name': 'Cohen',
    'city': 'Herzliya',
    'address': 'Hertzl 45',
    'phone': '0535645645',
    'email': 'david@hotmail.com',
    'age': 14
}

def is_person_using_gmail(person):
    email = person['email']
    return email.lower().endswith("@gmail.com")

def is_person_child(person):
    return person['age'] < 16

if __name__ == '__main__':
    print(is_person_using_gmail(person1))
    print(is_person_child(person1))