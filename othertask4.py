# 16.sum of first 10

n=int(input('enter number:'))
i=1
sum=0
while i <= n:
    sum += i
    i +=1
print("sum:",sum)

# 17. candidate selection

ch=input('enter name:')
selected=['rohan','rahul','sohan','rina','tina']
if ch in selected:
    print('congratulation.....you are selected')
else:
    print('better luck next time')

# 18. divisibility by 5

number=int(input("enter a number:"))
if number % 5 == 0:
    print("yes,number is divisible by 5")
    print("answer is:",(number/5))
else:
    print("number is not divisible by 5")

# 19. even odd number

num=int(input("enter any number: "))
if num%2 == 0:
    print(num,"is an even number")
else:
    print(num,"is an odd number")

# 20. factorial  with while

num=int(input('enter number:'))
factorial=1
i=1
while i <= num:
    factorial *= i
    i += 1
print("factorial:",factorial)