"""
Author: Noel Shaji
Date:22-11-2024
"""
list1=[]
list2=[]
even_list=[]
odd_list=[]
n1=int(input("Enter the no. of values: "))
for i in range(n1):
    i=int(input("Enter the values(list1): "))
    list1.append(i)
n2=int(input("Enter the no. of values: "))
for j in range(n2):
    j=int(input("Enter the values(list2): "))
    list2.append(j)
print("list1: ",list1)
print("list2: ",list2)
list3=list1+list2
print("combined_list:",list3)
for num in list3:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
even_list.sort()
odd_list.sort()
fin_list=even_list+odd_list
print("final list: ",fin_list)










