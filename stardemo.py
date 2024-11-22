print("INCREASED STAR PATTERN")
for i in range(6):
    for j in range(i,i+1):
        print(j*"*")
print("DECREASED STAR PATTERN")

for i in range(6,1,-1):
    for j in range(i-1,i):
        print(j*"*")
print("REVERSE HILL STAR PATTERN")
row=5
for i in range(row,0,-1): #row
    for j in range(row-i):#space
        print(" ",end="")
    for k in range(2*i-1):#pattern
        print("*",end="")
    print()

print("HILL STAR PATTERN\n")

for i in range(1,row+1): #row
    for j in range(row-i):#space
        print(" ",end="")
    for k in range(2*i-1):#pattern
        print("*",end="")
    print()










