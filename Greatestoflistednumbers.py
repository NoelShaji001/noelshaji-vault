limit=int(input("Enter n"))
number=int(input("Enter your number"))
small=number
big=number
while limit>1:
    number=int(input("Enter the number"))
    if number>big:
      big=number
    elif number<small:
        small=number
    limit=limit-1
print("The Big is",big)
print("The Small is",small)
















