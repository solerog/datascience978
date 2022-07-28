from class.student import Student

# Subclass

class DataStudent(Student):
    course = 'Data Science'

    def __init__(self, name, age, batch):
        super().__init__(name, age)
        self.batch = batch


data_student = DataStudent('Marti', 29, 978)
print(data_student.course)
print(data_student.__dict__)
