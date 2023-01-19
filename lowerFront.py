word = input("Enter a string: ")
lowerCase = []
upperCase = []

for char in word:
    if char.islower():
        lowerCase.append(char)
    elif char.isupper():
        upperCase.append(char)
print("".join(lowerCase)+"".join(upperCase))