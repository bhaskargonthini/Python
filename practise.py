def print_line(len=10, ch='-'):
    for i in range(len):
        print(ch,end='')
    else:
        print()
print_line(30,'*') #Passing values by position
print_line(20)
print_line()
print_line(ch='*') #Passing value by name
print_line(ch='*',len=15)