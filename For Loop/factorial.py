factorial = 1

number = int(input("Enter number to find factorial of: "))

for i in range(number, 0, -1):
    factorial *= i

print('Factorial:', factorial)