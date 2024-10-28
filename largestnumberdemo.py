"""
Author:Noel Shaji
Date:25-10-2024
Description:Write a Python program to find the largest of three numbers. The program should take three numbers as input from the user and determine which one is the largest. Use conditional statements to compare the numbers.
"""
a=int(input("Enter your first number"))
b=int(input("Enter your second number"))
c=int(input("Enter your third number"))

if a>b and a>c:
	print(a,"is the largest number")
elif b>c and  b>a:
	print(b,"is the largest number")
else:
	print(c,"is the largest number") 
	