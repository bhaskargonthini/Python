# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = 'Class A'


class B:
    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = 'Class B'


class C(A, B):
    def __init__(self):
        super().__init__()
    def showprops(self):
        print(self.foo)
        print(self.bar)
        print(self.name)
#python works as postional arguement
#so class a comes first in order so class c inherits this property here
c = C()
c.showprops()
