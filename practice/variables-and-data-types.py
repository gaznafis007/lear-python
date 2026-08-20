# variables and data types
# string, integer, float, boolean, none

name = "Gazi Nafis Md Abdullah"
age = 28
IsStudent = False
balance = 245.98

print('My name is ', name)
print("My age is", age)
if IsStudent:
    print("I am a student")
else:
    print("I am not a student")

print("My balance is $",balance)

# arithmetic operator
varOne = 10
varTwo = 20

print(varOne + varTwo)
print(varOne - varTwo)
print(varOne * varTwo)
print(varOne / varTwo)

# write a program to to input two numbers and print their sum.
num1 = float(input("Enter your first number :"))
num2 = float(input("Enter your second number :"))

sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)

# write a program to input the side of a square and print its area.
sideOfSquare = float(input("Enter the side of a square:"))

print("The area of the square is:", sideOfSquare **2)

# write a program to input two numbers and print their average.
numberOne = float(input("Enter your first number:"))
numberTwo = float(input("Enter your second number:"))
avg = (numberOne + numberTwo)/2
print("The avg of those numbers is: ", avg)

# write a program to input two int numbers, a and b. Print True if a si greater than  or equal to b. If not print False
a = int(input("Enter the value of a:"))
b = int(input("Enter the value of b:"))

print(a >= b)