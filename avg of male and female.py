n=int(input("enter the no of students:"))
total_m=0
total_f=0
male_num=0
female_num=0
for i in range(n):
	choice=input("enter male or female:")
	if choice=="male":
		height_m=float(input("enter the height of the male student:"))
		total_m+=height_m
		male_num+=1
	elif choice=="female":
		height_f=float(input("enter the height of the female student:"))
		total_f+=height_f
		female_num+=1
	else:
		print("Invalid entry")
avg_m=total_m/male_num
avg_f=total_f/female_num
print("male:",avg_m)
print("female",avg_f)
		
	


	