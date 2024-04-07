n=6
for i in range(n):
    for j in range(n+1):
        if (i==0 and j%3 !=0) or (i==1 and j%3==0) or (i -j)==2 or (i+j==8):
           print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

        
            
