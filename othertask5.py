# 1. Print numbers from 1 to 10

i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Print even numbers from 1 to 20

i = 2
while i <= 20:
    print(i)
    i += 2

# 3. Sum of first 10 natural numbers

i = 1
total = 0

while i <= 10:
    total += i
    i += 1

print("Sum:", total)

# 4. Multiplication table of a number

num = int(input("Enter a number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1

# 5. Reverse a number

num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

print("Reversed number:", reverse)