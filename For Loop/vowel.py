count = 0
string = input("Enter a string: ")

for i in range(len(string)):
    if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u' or string[i] == 'A' or string[i] == 'E' or string[i] == 'I' or string[i] == 'O' or string[i] == 'U':
        count = count + 1

print("Number of Vowels: ", count)