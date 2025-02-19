def greet (name):
    print(f'Hello, {name}!')

greet('nafis')

def add(num_one, num_two):
    return num_one + num_two

result = add(5,5)

print(result)

def subtract():
    num_one= float(input('enter first number: '))
    num_two= float(input('enter second number: '))
    return num_one + num_two

print(subtract())

def get_info():
    name= 'John Doe'
    age = 25
    return name, age

info_name, info_age = get_info()

print(info_age)

def multiply_by_you(num_one, num_two):
    return num_one, num_two, num_one * num_two

number_one= int(input("Enter number:"))
number_two= int(input("Enter another number: "))

one, two, result = multiply_by_you(number_one, number_two)

print(one, two, result)