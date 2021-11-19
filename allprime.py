def prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if(n % i == 0):
            return False
    else:
        return True
# a = int(input('enter the number:'))
# if(prime(a) == True):
#     print(f'{a} is prime number')
# else:
#     print(f'{a} is not prime number')
def allprime(m):
    for i in range(m):
        if prime(i):
            print(i, end = " ")
m = int(input('enter the number:'))
allprime(m)


