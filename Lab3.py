n = int(input("Enter the value of n: "))

a = 0

b = 1

count = 0

if n <= 0:

print("Please enter a valid integer")

elif n == 1:

print("Fibonacci series upto 1")

print(a)

else:
print("Fibonacci Sequence")

while (count < n):

print(a, end = " ")

c = a + b

# Updating the values of a and b by swapping

a = b

b = c

count += 1

Enter the value of n: 15

Fibonacci Sequence

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
