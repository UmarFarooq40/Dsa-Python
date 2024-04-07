#Alphabetic Pattern

n=5
for i in range(n):
    x=64
    for j in range(n-i):
        print(' ',end='')
    for j in range(i+1):
        x+=1
        print(chr(x),end=' ')
    print()