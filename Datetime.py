'''importing datetime module'''
from datetime import datetime

'''defining a class Person with attributes name, dob, and address'''
class Person:

    '''initializing the attributes of the Person class'''
    def __init__(self, name, dob,address):
        self.name = name
        self.dob = dob
        self.address = address

    '''calculating the age of the person'''
    def age(self):
        return self.find_age(datetime.today())

    '''finding the age of the person at a specific date'''
    def find_age(self, the_date):
        c_age=the_date.year-self.dob.year

        if (the_date.month,the_date.day)<(self.dob.month,self.dob.day):
            c_age-=1

        return c_age

    '''finding the date when the person will turn a specific age'''
    def date_for_age(self, the_age):
        target_year = self.dob.year + the_age

        return datetime(target_year, self.dob.month, self.dob.day)

'''getting user input for name, date of birth, and address'''    
person= Person(
    input("Enter the name: "),
    datetime(int(input("Enter birth year: ")), int(input("Enter birth month: ")), int(input("Enter birth day: "))),
    input("Enter the address: "))

'''displaying the person's details and calculated age'''
print(f"Name: {person.name}")
print(f"Age: {person.age()}")
print(f"Address: {person.address}")

'''getting user input for the target age to find the date they turn that age'''
target_age = int(input("Enter the age to find the date they turn that age: "))

turning_date = person.date_for_age(target_age)

print(f"Date they turn {target_age}: {turning_date}")
