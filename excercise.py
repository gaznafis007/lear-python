weight = input("What is your weight? ")
unit = input("(K) for kg, (L) for lbs? ").lower()
if unit == 'k':
    weight = str(float(weight) / 2.20462)
    print('Your weight is ' + weight + ' kg')
elif unit == 'l':
    weight = str(float(weight) * 2.20462)
    print('Your weight is ' + weight + ' lbs')
else:
    print("please enter a valid unit".capitalize())