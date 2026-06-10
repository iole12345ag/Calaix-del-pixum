print("Hello, this is a Unit converter between Fahreinheit and Celsius")
print("What do you want to convert?")

print("1. Fahreinheit to Celsius")
print("2. Celsius to Fahreinheit")

resposta = float(input("Pick the action number: "))

if resposta == 1:
    print("Type the temperature in Fahreinheit")
    temperature = float(input())
    temperatureInCelsius = (temperature-32)*5/9
    print(f"The temperature in Celcius is {temperatureInCelsius}")

if resposta == 2:
    print("Type the temperature in Celsius")
    temperature = float(input())
    temperatureInFahreinheit = (temperature*9/5)+32
    print(f"The temperature in Fahreinheit is {temperatureInFahreinheit}")
