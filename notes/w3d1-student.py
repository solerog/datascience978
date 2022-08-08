class Student:

    # Constructor
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def say(self) -> None:
        print(f'Hello my name is {self.name}')


# New class instance
student1 = Student('Roger', 34)
print(student1.__dict__)
print(student1.name)
student1.say()
