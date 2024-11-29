def re_gcd(num1,num2):
    if num1%num2==0:
        return num2
    else:
        return re_gcd(num2,num1%num2)
num1=int(input("num1"))
num2=int(input("num2"))
print(re_gcd(num1,num2))
