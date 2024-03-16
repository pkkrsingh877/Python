reverse = 0
number = int(input('Enter a number: '))

while number:
    digit = number % 10
    number = int(number / 10)
    reverse = 10 * reverse + digit

print('Reverse of digits: ', reverse)
