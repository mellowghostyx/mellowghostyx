#!/usr/bin/env python3

class User:
    def __init__(self, name, pronouns, language):
        self.name = name
        self.pronouns = pronouns
        self.language = language

    def say_hi(self):
        print(f"Hello! I'm {self.name}, and welcome to my readme!")

if __name__ == '__main__':
    ghostyx = User('Ghostyx', 'he/him', 'English')
    ghostyx.say_hi()
