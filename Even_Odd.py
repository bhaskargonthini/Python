even = []
odd = []
while True:
    num = int(input('enter  a number to check[0 to stop]:'))
    if num == 0:
        break
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
for n in even+odd:
    print(n, end = " ")

