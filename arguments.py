# Positional Arguments

def add(a, b):
    print(a + b)

add(10, 20)

# Keyword Arguments

def student(name, age):
    print(name, age)

student(age=18, name="Rahul")

# Default Arguments

def greet(name="Guest"):
    print("Hello", name)

greet("Amit")   # Hello Amit
greet()         # Hello Guest

# Variable-Length Arguments (*args)

def total(*numbers):
    print(sum(numbers))

total(10, 20, 30)
total(5, 15)

# Keyword Variable-Length Arguments (**kwargs)

def details(**data):
    for key, value in data.items():
        print(key, ":", value)

details(name="Ravi", age=20, city="Rajkot")

# Combined Example

def demo(a, b=5, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

demo(10, 20, 30, 40, name="Jay", city="Rajkot")