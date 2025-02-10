stars = int(input("How many stars you wanna see at most? "))

i = 1

while i < stars:
    print(i * '*')
    i+=1

while i >= 0:
    print(i * '*')
    i-=1