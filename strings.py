title = "python for Beginners."
file_type = input("Enter your file name: ")
print(title)
print(title.title())
print(title.capitalize())
print(title.casefold()) #kind of lowercase
print(title.count('o', 0, 9)) #find a character count in a variable of string
print(title.encode("utf-8", "strict"))
print(file_type.endswith('.py'))
print(title.find('n', 0))
print(title.index('y'))
print(title.upper())
print(title.lower())
print("FOR".casefold() in title.casefold())