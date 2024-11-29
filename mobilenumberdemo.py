"""
Author:Noel Shaji
Date:29-11-2024
"""
def is_mobile_number(number):
    if len(number)==10 and number[0] in "7""8""9":
        return True
    return False
number=(input("Enter your mobile number "))
if is_mobile_number(number):
    print(f"The mobile number{number} is valid")
else:
    print(f"The mobile number{number} is invalid")




