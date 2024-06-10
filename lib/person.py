#!/usr/bin/env python3


class Person:
    def __init__(self, name):
        self.name = name

    def adopt(self):
        print(f"{self.name} is the owner")


person1 = Person("Sophie")
print(person1.name)
person1.adopt()
