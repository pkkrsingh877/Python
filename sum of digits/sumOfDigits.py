sum = 0
number = int(input('Enter a number: '))

while number:
    digit = number % 10
    sum = sum + digit
    number = int(number / 10)

print("Sum of Digits: ", sum)
