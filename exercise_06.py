from numpy import*
row = int(input("Enter a row num from 1 to 5: "))
column = int(input("Enter a column from 1 to 5: "))

m = matrix('0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0; 0 0 0 0 0')

m[row-1,column-1] = 1
print(m)