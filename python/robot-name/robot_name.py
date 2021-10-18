from random import choices
from string import ascii_uppercase, digits

names = []

class Robot:
    def __init__(self):
        self.__generate_name()
    def reset(self):
        self.__generate_name()
    def __generate_name(self):
        prefix = choices(ascii_uppercase, k=2)
        suffix = choices(digits, k=3)
        self.name = "".join(prefix + suffix)
        if self.name in names:
            self.__generate_name()
        else:
            names.append(self.name)

