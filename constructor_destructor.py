class Student:
    def __init__(self,nam,clas):
        self.name = nam
        self.Class = clas
    def info(self):
        print("Student name is : ",self.name)
        print("Class of student is : ",self.Class)
    def __del__(self):
        # self.edu = "Matrix"
        print(f"Now object 1 is ending and having class {self.Class}")

obj1 = Student("Abdullah","12 th")
obj1.info()
del obj1

class Teacher:
    def __init__(self,nam,clas):
        self.name = nam
        self.Class = clas
    def info(self):
        print("Teacher name is : ",self.name)
        print("Qualification of teacher is : ",self.Class)
    def __del__(self):
        print("Now object 2 is ending")

obj2 = Teacher("Sir irfan malik","BS AI")
obj2.info()
