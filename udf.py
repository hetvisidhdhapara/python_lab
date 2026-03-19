# function with no parameters and no return

def greet():
    print("welcome to python programming")
greet()

# function with parameters

def greet(name):
    print("hello",name)
    print("welcome to our program!")

greet("asha")
greet("ravi")

# function with return value

def add(a,b):
    c=a+b
    return c

result=add(5,3)
print("result=",result)

# function to check even or odd

def even(num):
    if num % 2==0:
        return True
    else:
        return False

print(even(4))
print(even(7))