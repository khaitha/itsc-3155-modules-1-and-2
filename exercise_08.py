original_list = []
count = 1

# Take in 10 integers from the user
for i in range(10):
    print("Enter integer", count, ":")
    original_list.append(int(input()))
    count += 1

# Create a new list with only elements that appear once
unique_list = []
for i in original_list:
    if original_list.count(i) == 1:
        unique_list.append(i)

# Print both lists
print("Original List:", original_list)
print("Nums that appear once :", unique_list)