string = input("Enter a string: ")
characters = list(string)
print(characters)
split_list = []

for i in range(0, len(characters), 3):
    split_list.append(characters[i:i+3])

print(split_list)