def max_numbers(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num3:
        return num2
    else:
        return num3
num1=int(input("Enter your first number: "))
num2=int(input("Enter your second number: "))
num3=int(input("Enter your third number: "))
result=max_numbers(num1,num2,num3)
print("The maximum number is ",result)


