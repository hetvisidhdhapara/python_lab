# 11. square
def square(n):
    return n * n

num = 5
print(square(num))

# 12. odd numbers from 1 to 10

for i in range(1,21):
    if i % 2 != 0:
        print(i,end=" ")

# 13. even numbers between 50 to 100

x=50
while(x<=100):
    print(x,end=" ")
    x += 2
# 14.


# 15. keep asking until correct password

password = ""
while password != "atmiya":
    password=input("enter the password: ")
    print("access granted!")
