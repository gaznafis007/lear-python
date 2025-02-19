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

amount = float(input('Enter your amount: '))
currency = input("Enter $ for usd, enter T for BDT: ").lower()
if(currency == '$'):
    conversion_result = amount / 121.21
    print(f'{amount} BDT is {conversion_result} in USD')
elif (currency == 't'):
    conversion_result = amount * 121.21
    print(f'{amount} USD is {conversion_result} in BDT')
else:
    print('Please enter the currency correctly')

