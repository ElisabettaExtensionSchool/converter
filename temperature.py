# (Celsius * 9/5) + 32 = Fahrenheit)

# cels = 7.32
# far = (cels * 9/5) + 32
# print(far)

# def converter(celsius):
#     result = (celsius * 9/5) + 32      #or: return (celsius *9/5) + 32
#     message = str(celsius) + " degrees Celsius are " + str(result) + " degrees Fahrenheit."
#     return message
# print (converter(21.5))
# print (converter(-7))
# print (converter(11))
# print (converter(0))

#with user input
def converter(celsius):
    result = (celsius * 9/5) + 32      #or: return (celsius *9/5) + 32
    message = str(celsius) + "°C are " + str(result) + "°F."
    return message
user = input("What's the temperature in °C that you want to convert? ")
print (converter(float(user)))


# celsius = input("What's the temperature in °C that you want to convert? ")
# result = (float(celsius) * 9/5) + 32 
# print(celsius + "°C are " + str(result) + "°F.")

