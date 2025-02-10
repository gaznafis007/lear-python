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