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

class product_info:
    def __init__(self, name, price, description, qty):
        self.name = name
        self.price = price
        self.description = description
        self.qty = qty
    
    def product_printer(self):
        print(f'product name: {self.name}, product price: {self.price}, qty left: {self.qty}')


product_one = product_info('nike air jordan', '3500 USD', 'What  shoe', 7 )

product_one.product_printer()