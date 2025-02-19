x=10
print(x)
x= 10 + 10
print(x)
y = x + 20
print(y)
y = x * y
print(y)
y = y - 100
print(y)
y = y / 10
print(y)
z = y / 3
y = y // 3
print(y, z)
y = y ** 2
z = z ** 2
print(y, z)

p = (x+y)*2/z
print(p)

a = int(input('Enter a number: '))
b = int(input('Enter second number: '))
c = int(input('Enter final number: '))

print(f'add {a + b}')
print(f'subtract {a - b}')
print(f'multiply {a * b}')
print(f'division {a / b}')
print(f'approx division {a // b}')
print(f'power {(a + b) ** c}')
print(f'reminder {b % c}')