binary = ''
power = 0

decimal = int(input('Enter a decimal number: '))

while decimal:
    digit = decimal % 2
    binary = str(digit) + binary
    decimal = int(decimal / 2)
    power = power + 1

print('Binary Equivalent:', binary)
