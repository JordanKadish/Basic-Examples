# Jordan Kadish
# 26/10/2017
# Person OOP class
# Testing out pep8 formatting
"""Testing out this pep8 stuff. looks a bit hideous tbqh"""


class Person:
    """This is a generic person class. """

    def __init__(self, name, mid_name, surname, age):
        self.name = name
        self.mid_name = mid_name
        self.surname = surname
        self.age = age

    def __str__(self):
        return self.name + " " + self.surname + ", " + str(self.age) + \
            " years old"

    def initials(self):
        """returns the person's initials, separated by a comma"""
        return self.name[0] + "." + self.mid_name[0] + "." + self.surname[0]

    def happy_birthday(self):
        """ages the person by one year"""
        self.age += 1


if __name__ == '__main__':
    PERSON_P = input().strip().split()
    print(Person(PERSON_P[0], PERSON_P[1], PERSON_P[2], PERSON_P[3]))
