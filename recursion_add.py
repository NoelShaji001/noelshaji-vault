def re_add(num1,num2):#recursive addition of numbers
    if num2==0:
        return num1
    else:
        return re_add(num1+1,num2-1)
num1=int(input("num1="))
num2=int(input("num2="))
print(re_add(num1,num2))
