n=int(input("Enter a number: "))# user has to unput a number.
if n%2!=0:
	print("Weird")
elif n%2==0 and n>=2 and n<=5:
	print("Not Weird")
elif n%2==0 and n<=6 and n>=20:
	print ("Weird")
elif n%2==0 and n>20 and n<=100:
	print("Not Weird")# constraint:1<=n<=100

