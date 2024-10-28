"""
Author:Noel Shaji
Date:28-10-2024
Description:Write a menu-driven python program that allows user to convert temperatures between
Celsius and Fahrenheit.
"""
while True:
    print("\n1.\tConvert Celsius to Fahrenheit")
    print("2.\tConvert Fahrenheit to Celsius")
    print("3.\tExit the program")
    choice=int(input("Enter your choice"))
    if choice == 1:
        celsius = int(input("Enter a temperature in celsius:"))
        fahrenheit_value= (celsius * 9/5) + 32
        print(f"The equivalent temperature in Fahrenheit is {fahrenheit_value}")
    elif choice ==2:
        fahrenheit=int(input("Enter the temperature in fahrenheit:"))
        celsius_value=(fahrenheit - 32) * 5/9
        print(f"The equivalent temperature in celsius is {celsius_value}")
    elif choice == 3:
        break

    else:
        print("Invalid input")




