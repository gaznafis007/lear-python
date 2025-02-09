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