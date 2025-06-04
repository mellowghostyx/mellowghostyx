# 👋 Hi! Hello! Welcome!

```python
class User:
    def __init__(self, name, pronouns, age, languages):
        self.name = name
        self.pronouns = pronouns
        self.age = age
        self.languages = languages
    
    def greet(self):
        print("Hello! I'm", self.name + ", and welcome to my readme!")

ghostyx = User(
    name="Ghostyx",
    pronouns="he/him",
    age=21,
    languages=["en-US"]
)

ghostyx.greet()
```

```
Hello! I'm Ghostyx, and welcome to my readme!
```
