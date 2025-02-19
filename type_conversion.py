birth_year = input("What is your birth year? ")

age = 2025 - int(birth_year)

print("you are", age, "years old.")

# exercise

first_number = input("enter the first number: ")
second_number = input("enter the second number: ")

# result = int(first_number) + int(second_number)
result = float(first_number) + float(second_number)

print("summation is:", result)

is_online = True

converted_text = str(is_online)
print(is_online, converted_text)

language = int(input('Please enter your language course marks: '))
history = int(input('Please enter your history course marks: '))
math = int(input('Please enter your math course marks: '))

total_marks = language + history + math
avg_result = str(total_marks / 3)

print('your average result of the marks is' + avg_result + 'and total marks is' + str(total_marks))
