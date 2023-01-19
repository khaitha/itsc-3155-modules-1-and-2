firstList = []
secondList = []
commonList = []

for i in range(5):
    firstInput = int(input("Enter a number for the first list: "))
    firstList.append(firstInput)
print("First List: ",firstList)

for i in range(5):
    secondInput = int(input("Enter a number for the second list: "))
    secondList.append(secondInput)
print("Second List: ", secondList)

commonList = set(firstList) & set(secondList)
print("Common List:", commonList)