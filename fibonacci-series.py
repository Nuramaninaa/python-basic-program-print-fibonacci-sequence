#python program to print fibonacci seried

#input from user
n = int(input("Enter the number : "))

a,b = 0,1

while b<20:
    print(b)
    a,b = b,a+b
    