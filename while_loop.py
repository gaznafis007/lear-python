stars = int(input("How many stars you wanna see at most? "))

i = 1

while i < stars:
    print(i * '*')
    i+=1

while i >= 0:
    print(i * '*')
    i-=1

def star_sqr_box (size):
    i = 0
    while i < int(size):
        print(size * '*')
        i+=1

star_sqr_box(stars)

def inverse_stars (size):
    i = size
    while (i > 1 ):
        print(i * '^')
        i-=1

    while(i <= size):
        print(i * '^')
        i+=1

inverse_stars(stars)