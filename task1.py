# 1.calulate simple interest

principal=float(input("enter principal amount:"))
rate=float(input("enter rate of interest:"))
time=float(input("enter time(in years):"))
simple_interest = (principal * rate * time) /100
print("simple interest is :",simple_interest)

# 2.find max of 2 no.

a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a>b:
    print("maximum number is :",a)
else:
    print("maximum number is :",b)

# 3. print no. 1 to 5
for i in range(1,6):
  print(i)

  # 4. find length of a string

text=input("enter a string:")
print("length of the string is :",len(text))

# 5.print a welcome message
print("welcome")

# 6.print 1st character of a string
text=input("enter a string:")
print("first character is :",text[0])

# 7.print last character of a string
text=input("enter a string:")
print("last character is :",text[-1])

# 8. check a positive or negative no.
num=int(input("enter a number:"))
if num>0:
    print("number is positive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")

# 9. add 3 no.
a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
sum=a+b+c
print("sum of three number is :",sum)

# 10. take a input from user
name=input("enter your name:")
print("name is :",name)