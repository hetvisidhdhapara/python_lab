#1.print number from 1 to 5
i=1
while i<=5:
    print(i)
    i=i+1

#2.sum of numbers take user input
num=int(input("enter number:"))
i=1
s=0
while i<=num:
    s=s+i
    i=i+1
    print("sum=",s)
#3.print odd number between 1 and 20
num = 1

while num <= 20:
    print(num)
    num = num + 2   #simple syntax

#3.print odd number between 1 and 20

num=1
while num<=20:
    if num % 2 != 0:
        print(num)
    num=num+1        #if syntax

#4.print table of 4
num=4
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1

#5.print revers number
i=10
while i>=1:
    print(i)
    i=i-1

#6.find largest number in the list 
#7.print even number between 1 and 20.
i=1
while i<=20:
 if i%2==0:
    print(i)
 i=i+1
