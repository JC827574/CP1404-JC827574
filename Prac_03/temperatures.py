"""
Program to convert Celsius to Fahrenheit and vice versa
"""


def main():
    get_input = (input("Which Unit would you like to convert from ? press C (celsius) or F (Fahrenheit): "))
    if get_input == "C":
        celsius_to_fahrenheit()
    elif get_input == "F":
        fahrenheit_to_celsius()
    else:
        print("Enter a Valid Option")


def celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))


def fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: C", round(celsius))



main()
