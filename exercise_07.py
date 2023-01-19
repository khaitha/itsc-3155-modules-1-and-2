numbers = []
even_numbers = []

while True:
    user_input = input("Enter an integer or type 'QUIT' to stop: ")
    if user_input == "QUIT":
        break
    else:
        number = int(user_input)
        numbers.append(number)
        if number % 2 == 0:
            even_numbers.append(number)

print("List of all numbers entered:", numbers)
print("List of even numbers:", even_numbers)