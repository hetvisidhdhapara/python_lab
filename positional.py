# BASIC POSITIONAL ARGUMENT
def add(a,b):
    print("a =",a)
    print("b =",b)
    return a+b
result=add(2,4)
print("sum= ",result)

#student information

def student_info(name,roll,marks):
    print("name=",name)
    print("roll=",roll)
    print("marks=",marks)
student_info("hetvi",57,99)

#simple interest

def simple_interest(p,r,n):
    si=(p*r*n)/100
    print("simple_interest: ",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)

#area of circle

def ar_circle(r):
    a_circle=3.14*r*r
    print("area of circle: ",a_circle)
ar_circle(1.8)

#check number positive or negative or zero

def check_value(no):
    if(no>0):
        print("positive")
    elif(no<0):
        print("negative")
    else:
        print("zero")

check_value(29)
check_value(0)
check_value(-23)

# odd or even 

def odd_even(no):
    if(no%2==0):
        print("even")
    else:
        print("odd")

odd_even(20)
odd_even(15)

# arithmatic operation substraction,multiplication and division

def addition(a,b):
    add=a+b
    print("addition= ",add)
addition(20,5)

def substraction(a,b):
    sub=a-b
    print("substraction=",sub)
substraction(20,5)

def multi(a,b):
    mul=a*b
    print("multiplication= ",mul)
multi(20,5)

def division(a,b):
    div=a/b
    print("division= ",div)
division(20,5)

