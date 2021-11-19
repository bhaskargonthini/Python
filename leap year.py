def checkleapyear(year):
    if((year % 4 == 0 & year % 100!=0)| year % 400 == 0):
        print('%d it is a   leap year' %year)
    else:
        print('%d it is not leap year' %year)
x = int(input('enter the year:'))
checkleapyear(x)


