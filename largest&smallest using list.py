n=int(input("enter the no. of values: "))
numbers=[]
for i in range(n):
	i=int(input("enter the number"))
	numbers.append(i)
	i+=1
numbers.sort(reverse=False)
print(numbers)
print(f"The smallest number is: {numbers[0:1]}")
num1=len(numbers)
print(f"The largest number is: {numbers[num1-1:]}")


