# 1.Print numbers 1 to 10

for i in range(1, 11):
    print(i)

# 2.Print even numbers from 1 to 20

for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3.Print the multiplication table of a number

num = 5
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# 4.Find the sum of numbers from 1 to 100

total = 0
for i in range(1, 101):
    total += i
print(total)

# 5.Count vowels in a string

text = "hello world"
count = 0

for char in text:
    if char in "abcde":
        count += 1

print(count)