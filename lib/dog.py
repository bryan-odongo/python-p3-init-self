#!/usr/bin/env python3


class Dog:

    def __init__(self, name="Mutt", breed="Mutt"):
        self.name = name
        self.breed = breed

    def adopt(self):

        print(f"fido owner is {self.name}")


fido = Dog("sophie")
print(fido.name)
print(fido.breed)
snoopy = Dog()
fido.adopt()
