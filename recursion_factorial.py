def re_factorial(n):#recursive factorial
    if n==1:
        return 1
    else:
        return n*re_factorial(n-1)
n=int(input("Enter your number:"))
print(re_factorial(n))
