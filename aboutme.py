# The actual code used in my README.md
# inspired by: https://github.com/Zhenye-Na/Zhenye-Na

class User:
    def __init__(self, name, pronouns, age, languages):
        self.name = name
        self.pronouns = pronouns
        self.languages = languages
    
    def greet(self):
        print("Hello! I'm", self.name + ", and welcome to my readme!")

ghostyx = User(
    name="Ghostyx",
    pronouns="he/him",
    languages=["en-US"]
)

ghostyx.greet()
