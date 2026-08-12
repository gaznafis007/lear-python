name='john doe'
age=28
status=True

print(f'{name} is {age} years old and is {"a new patient" if not status else "not a new patient"}')
print(f'{name} is {age} years old and is {"adult" if age >= 18 else "not adult"}')
print(f'Hello, {name}')
print(f'{name} is {age} years old')
print(f'{name} is {age} years old and is {"a new patient" if not status else "not a new patient"}')