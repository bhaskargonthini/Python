class cal1:
    def add(self, a, b):
        return a+b
class cal2:
    def mult(self, a, b):
        return a*b
class derived(cal1, cal2):
    def divide(selfself, a, b):
        return a/b
d = derived()
print(issubclass(derived,cal1))
print(issubclass(cal1,cal2))