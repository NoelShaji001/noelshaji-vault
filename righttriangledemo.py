"""
Author:Noel Shaji
Date:29-11-2024
"""
def check_right_triangle(s):
    s.sort(reverse=True)
    if s[0]**2==s[1]**2+s[2]**2:
        return True
    return False
s=[]
a=int(input("Enter the side length1:"))
b=int(input("Enter the side length2:"))
c=int(input("Enter the side length3:"))
s.append(a)
s.append(b)
s.append(c)
if check_right_triangle(s):
    print("The given sides are part of right triangle")
else:
    print("The given sides are not part of right triangle")