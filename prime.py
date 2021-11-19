def prime(x):
    if(x>1):
        for i in range(2, x):
            if(x % i == 0):
                # flag = True
                y = 0
                break
    # if (flag == True):
    if (y == 0):
        print('%d is not a prime number' %x)
    else:
        print('%d is a prime number' %x)
a = int(input('enter the number:'))
prime(a)
