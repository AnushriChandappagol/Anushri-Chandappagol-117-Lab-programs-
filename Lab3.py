for t in range(1,101):

for i in range(1,11):

print(str(t).zfill(2),'x',str(i).zfill(2),'=',str(t*i).zfill(3))

print('-'*15)

Show hidden output

a = [1,2,3]

a.append(5)

a

[1, 2, 3, 5]

Mean, Variance and Standard Deviation

# Read N numbers from the console and create a list.

# Develop a program to print mean, variance and standard deviation

n = int(input("Enter the number students: "))

list1 = []

for i in range(n):

marks = int(input("Enter marks of each student in python: "))

list1.append(marks)

print("List containing marks of student: ", list1)

print("-"*50)

# Finding Mean

sum = 0 # Initialize

for i in list1:

sum += i

print("Sum of all the elements in the list: ", sum)

x_bar = sum/len(list1)

print("Mean: ", x_bar)

# Finding Variance

var = 0 # Initialize

for i in list1:

var = var + ((i - x_bar)**2)/len(list1)

print("Variance: ", var)

# Finding Standard Deviation

std_dev = var**0.5

print("Standard Deviation: ", std_dev)
