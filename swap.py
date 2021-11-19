# a = int(input('enter the number:'))
# T = int(input('enter number of times you want to check:'))
# i = 0
# for i in T:
#     a = int(input('enter the number:'))
#     if(a>0):
#         print('the number is positive')
#     elif(a<0):
#         print('the number is negative')
#     else:
#         print('the number is zero')
# a,b = 12,13
largest = 0
while True:
    num = int(input("enter a number[0 to stop]:"))
    if num == 0:
        break
    if num>largest:
        largest = num
    print(f'Largest number is {largest}')



