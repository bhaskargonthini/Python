# def power(n):
#     for i in range(n):
#         print(f'2 raised to power {i} is:', 2**i)
# x = int(input('enter number of terms:'))
# power(x)

#  Display the powers of 2 using anonymous function

terms = 10

# Uncomment code below to take input from the user
# terms = int(input("How many terms? "))

# use anonymous function
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
