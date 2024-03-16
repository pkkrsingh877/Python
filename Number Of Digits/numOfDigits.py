count = 0
number = int(input('Enter a number: '))

while number > 0:
    count = count + 1
    number = int(number / 10)

print('Number of Digits:', count)
