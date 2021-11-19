# class Emp:
#     "this is developed by bobby"
#     def __init__(self):
#         self.name = "jyothsna"
#         self.sal = 50000
#         self.design = 'developer'
#     def display(self):
#         print('name is :', self.name)
#         print('salary is :', self.sal)
#         print('designation is', self.design)
# e = Emp()
# e.display()
# class Emp:
#     "this is developed by bobby"
#     def __init__(self,name,sal,desg):
#         self.name = name
#         self.sal = sal
#         self.desg = desg
#     def display(self):
#         print('name is:', self.name)
#         print('salary is :', self.sal)
#         print('designation is:', self.desg)
# # e0 = Emp()
# # e0.display()
# e = Emp('raghu',25000,'programmer')
# e.display()
# e1 = Emp('uday',60000,'designer')
# e1.display()
# class Test:
#     def __init__(self):
#         print('constructor executed')
#     def m1(self):
#         print('method execution')
# t = Test()
# t1 = Test()
# t2 = Test()
# t.m1()
class Student:
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name
        self.marks = marks
    def display(self):
        print('rollno:{}\n name:{}\n marks:{}\n'.format(self.rollno,self.name,self.marks))
s1 = Student(111,'uday',95)
s1.display()
s2 = Student(222,'sushma',97)
s2.display()



