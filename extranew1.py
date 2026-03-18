#print a welcome message

print("Hello,welcome to python programming")

#Take two numbers from the user and perform addition.

num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
result=num1+num2
print("sum =",result)

#Check if a number is even or odd.

num=int(input("enter a number: "))

if num % 2 == 0:
    print("even number")
else:
    print("odd number")

#Print the multiplication table of a number.

num=int(input("enter a number: "))
for i in range(1,11):
    print(num, "x" ,i,"=",num*i)

#Find the Largest Number
#Compare three numbers

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

largest=max(a,b,c)

print("largest number is:",largest)

