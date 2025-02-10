class personal_info:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f'Hello {self.name}, you are {self.age} years old')

person_one = personal_info('John Doe', 27)

print(person_one.age)
print(person_one.name)
person_one.greet()

class Math:
    def add(a, b):
        return a + b
    def subtract(a, b):
        return a - b
    def multiply(a, b):
        return a * b
    def divide (a, b):
        return a / b
    def mod(a, b):
        return a % b
    def pow(a, b):
        return a ** b

print(Math.add(5,5))
print(Math.subtract(5,15))
print(Math.multiply(5,5))
print(Math.mod(5,5))
print(Math.pow(5,5))