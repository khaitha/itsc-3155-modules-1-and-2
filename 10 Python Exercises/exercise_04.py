size =  int(input("Enter a number: "))
List = []
count = 1
total = 0
for i in range(size):
    enterNum = float(input("Enter number "+str(count)+": "))
    List.append(enterNum)
    total += enterNum
    count += 1
print("Average:", total/size)