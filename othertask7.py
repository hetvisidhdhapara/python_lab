# 6.Reverse a string using a loop

text = "python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(reversed_text)

# 7.Find prime numbers in a range

for num in range(2, 21):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# 8.Create a pattern

for i in range(1, 6):
    print("*" * i)

# 9.Nested loop – multiplication table (1 to 5)

for i in range(1, 6):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()
