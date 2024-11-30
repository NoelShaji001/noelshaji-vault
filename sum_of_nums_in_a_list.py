def add_num(numbers):
    total=0
    for i in numbers:
        total+=i
    print(total)
numbers=[]
n=int(input("enter a no.of elements"))
for j in range(n):
    n1=int(input("enter a number"))
    numbers.append(n1)
print(add_num(numbers))