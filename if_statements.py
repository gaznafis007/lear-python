temperature = int(input("What is the temperature in your area? "))

if temperature >= 35:
    print(str(temperature) + " is a hot temperature, please drink plenty of water" )
elif temperature < 35 and temperature >= 17:
    print(str(temperature) + " is a good weather, have an nice day")
elif temperature < 17 and temperature >= 10:
    print(str(temperature) + " it's becoming cold.")
elif temperature < 10 and temperature == 3:
    print(str(temperature) + " It's been cold outside. Close the window")
else:
    print(str(temperature) + " is extreme weather condition")


marks = int(input('Enter your marks to get the grade: '))

if marks >= 80:
    print('Congratulations! you got A+')
elif marks < 80 and marks >= 70:
    print('Congratulations! you got A')
elif marks < 70 and marks >= 60:
    print('Congratulations! you got A-, push more')
elif marks < 60 and marks >= 50:
    print("You got B, work hard")
elif marks < 50 and marks >= 40:
    print("You passed, but need to concentrate more")
else:
    print("Sorry, You failed, please try again")